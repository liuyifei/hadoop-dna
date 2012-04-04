package org.hadoop.dna.netflow;

import org.apache.hadoop.io.*;
import java.io.*;

public class FlowWritable implements Writable {
    // field
    private float stime;
    private float etime;
    private long bcount_up;
    private long bcount_dn;
    private long pcount_up;
    private long pcount_dn;
    private static int timeout = 7200;

    public FlowWritable() {

    }

    public FlowWritable(FlowWritable f) {
	stime = f.stime;
	etime = f.etime;
	bcount_up = f.bcount_up;
	bcount_dn = f.bcount_dn;
	pcount_up = f.pcount_up;
	pcount_dn = f.pcount_dn;
    }

    public String toString() {
	return String.format("%f %f %d %d %d %d", stime, etime, bcount_up, bcount_dn, pcount_up, pcount_dn); 
    }

    public FlowWritable(float s, float e, long b1, long b2, long p1, long p2) {
	stime = s;
	etime = e;
	bcount_up = b1;
	bcount_dn = b2;
	pcount_up = p1;
	pcount_dn = p2;
    }

    public void sum(FlowWritable f1) {
	bcount_up += f1.bcount_up;
	bcount_dn += f1.bcount_dn;
        pcount_up += f1.pcount_up;                                                                               
	pcount_dn += f1.pcount_dn;                                                                           
	
    }
  
    public void merge(FlowWritable f1) {
	if (f1.stime < stime) stime = f1.stime;
	if (etime > f1.etime) etime = f1.etime;

	bcount_up += f1.bcount_up;
	bcount_dn += f1.bcount_dn;
	pcount_up += f1.pcount_up;
	pcount_dn += f1.pcount_dn;

    }

    public boolean mergeable(FlowWritable f1) {
	// compare self vs f1
	if (stime <= f1.stime) {
	    // f1 is mergeable
	    if (f1.stime <= etime + timeout) {
		return true;	
	    }
	}
	else {
	    if (stime <= f1.etime + timeout) {
		return true;
	    }
	} 
	return false;
    }


    public void write(DataOutput out) throws IOException {
	out.writeFloat(stime);
	out.writeFloat(etime);
	out.writeLong(bcount_up);
	out.writeLong(bcount_dn);
	out.writeLong(pcount_up);
	out.writeLong(pcount_dn);

    }


	public static FlowWritable read(DataInput in) throws IOException {
	FlowWritable f = new FlowWritable();
	f.readFields(in);
	return f;
    }

    public void readFields(DataInput in) throws IOException {
	stime = in.readFloat();
	etime = in.readFloat();
	bcount_up = in.readLong();
	bcount_dn = in.readLong();
	pcount_up = in.readLong();
	pcount_dn = in.readLong();
    }

}

