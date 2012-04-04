package org.hadoop.dna.netflow;

import org.hadoop.dna.netflow.Layer3Writable;

import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Map;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.commons.logging.LogFactory;
import org.apache.commons.logging.Log;

public class Flow {
    private static final Log LOG = LogFactory.getLog(Flow.class);
    public static long convertToInt(String ip) {
        String[] addrArray = ip.split("\\.");
        long num = 0;
        for (int i = 0; i < addrArray.length; i++) {
            int power = 3 - i;
            num += ((Integer.parseInt(addrArray[i]) % 256 * Math.pow(256, power)));
        }
        return num;
    }

    private static long sip = convertToInt("14.63.100.0");
    private static long eip = convertToInt("14.63.255.255");


    public static class FlowMapper 
	extends Mapper<Object, Text, Text, Layer3Writable>{
    
	public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
	String line = value.toString();
	String[] array = line.split("[ ]");
	String flow = "";
	/*
	 * format : srcip(0), srcport(1), proto(2), dstip(3), dstport(4), stime(5), elapse(6), packets(7), bytes(8)
	 * format : 1|1311029765.716|0|184.172.243.22|14.63.237.2|80|21563|6|1|46
	 *       dir(0), stime(1), elapse(2), sip(3), dip(4), sport(5), dport(6), proto(7), pcount(8), bcount(9)
	 */
	long src = convertToInt(array[0]);
	long dst = convertToInt(array[3]);
	int bcount = Integer.parseInt(array[8]);
	int pcount = Integer.parseInt(array[7]);
	int bcount_up = 0;
	int bcount_dn = 0;
	int pcount_up = 0;
	int pcount_dn = 0;
	if (src >= sip && src <= eip) {
	    // uplink traffic
	    //LOG.info("uplink");
	    //LOG.info(array[0]);
	    //context.write(new Text(array[0]), new IntWritable(bcount));
	    bcount_up = bcount;
	    pcount_up = pcount;
	    bcount_dn = 0;
	    pcount_dn = 0;
	    //mValue.put(new Text("up_bytes"), new IntWritable(bcount));
	    //mValue.put(new Text("up_packets"), new IntWritable(pcount));
	    //mValue.put(new Text("dn_bytes"), new IntWritable(0));
	    //mValue.put(new Text("dn_packets"), new IntWritable(0));
	    flow = array[0]+"_"+array[3];
	    //context.write(new Text(array[0]), mValue);
	}
	else {
	    //LOG.info("downs");
	    //LOG.info(array[3]);
	    //context.write(new Text(array[3]), new IntWritable(bcount));
	    bcount_up = 0;
	    pcount_up = 0;
	    bcount_dn = bcount;
	    pcount_dn = pcount;
	    //mValue.put(new Text("up_bytes"), new IntWritable(0));
	    //mValue.put(new Text("up_packets"), new IntWritable(0));	    
	    //mValue.put(new Text("dn_bytes"), new IntWritable(bcount));
	    //mValue.put(new Text("up_packets"), new IntWritable(pcount));
	    flow = array[3] + "_" + array[0];
	    //context.write(new Text(array[3]), mValue);
	}
	context.write(new Text(flow), new Layer3Writable(bcount_up, bcount_dn, pcount_up, pcount_dn));
	/*
	if (array.length == 9) {
	    String direction = array[0];
	    String flow_indicator = "";

	    if (direction == "0") {
		flow_indicator = array[3] + "_" + array[5] + "_" + array[7] + "_" + array[6] + "_" + array[4];
	    } else if(direction == "1") {
		flow_indicator = array[4] + "_" + array[6] + "_" + array[7] + "_" + array[5] + "_" + array[3];	
	    }

	    // flow value
	    //Integer stime = Integer.parseInt(array[1]);
	    //Integer etime = stime + Integer.parseInt(array[2]);
	    Integer bcount = Integer.parseInt(array[9]);
	    //Integer pcount = Integer.parseInt(array[8]);
	    //Integer merge = 0;
	    //MapWritable mValue = new MapWritable();
	    //mValue.put(new Text("stime"), new IntWritable(stime));
	    //mValue.put(new Text("etime"), new IntWritable(etime));
	    //mValue.put(new Text("bcount"), new IntWritable(bcount));
	    //mValue.put(new Text("pcount"), new IntWritable(pcount));

	    context.write(new Text(flow_indicator), new IntWritable(bcount));
	}
	*/
    }
  }
  
    public static class FlowReducer 
      extends Reducer<Text,Layer3Writable,Text,Layer3Writable> {
 

	public void reduce(Text key, Iterable<Layer3Writable> values, 
			   Context context
			   ) throws IOException, InterruptedException {
	    
	    Layer3Writable sum = new Layer3Writable();
	    for (Layer3Writable val : values) {
		sum.sum(val);
	    }	
	    context.write(key, sum);
	}
    }
    
    public static void main(String[] args) throws Exception {
	Configuration conf = new Configuration();
	String[] otherArgs = new GenericOptionsParser(conf, args).getRemainingArgs();
	if (otherArgs.length != 2) {
	    System.err.println("Usage: wordcount <in> <out>");
	    System.exit(2);
	}
	Job job = new Job(conf, "flow generator");
	job.setJarByClass(Flow.class);
	job.setMapperClass(FlowMapper.class);
	job.setCombinerClass(FlowReducer.class);
	job.setReducerClass(FlowReducer.class);
	job.setOutputKeyClass(Text.class);
	job.setOutputValueClass(Layer3Writable.class);
	FileInputFormat.addInputPath(job, new Path(otherArgs[0]));
	FileOutputFormat.setOutputPath(job, new Path(otherArgs[1]));
	System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
