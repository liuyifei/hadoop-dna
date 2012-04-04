package org.hadoop.dna.netflow;

//import com.cloud.flow.WritableComparable;
import org.apache.hadoop.io.*;
import java.io.*;

public class Layer3Writable implements Writable {
    // field
    private int bcount_up;
    private int bcount_dn;
    private int pcount_up;
    private int pcount_dn;

    public Layer3Writable() {

    }

    public Layer3Writable(Layer3Writable f) {
	bcount_up = f.bcount_up;
	bcount_dn = f.bcount_dn;
	pcount_up = f.pcount_up;
	pcount_dn = f.pcount_dn;
    }

    public String toString() {
	return String.format("%d %d %d %d", bcount_up, bcount_dn, pcount_up, pcount_dn); 
    }

    public Layer3Writable(int b1, int b2, int p1, int p2) {
	bcount_up = b1;
	bcount_dn = b2;
	pcount_up = p1;
	pcount_dn = p2;
    }

    public void sum(Layer3Writable f1) {
	bcount_up += f1.bcount_up;
	bcount_dn += f1.bcount_dn;
        pcount_up += f1.pcount_up;                                                                               
	pcount_dn += f1.pcount_dn;                                                                           
	
    }
  
    public void merge(Layer3Writable f1) {
	bcount_up += f1.bcount_up;
	bcount_dn += f1.bcount_dn;
	pcount_up += f1.pcount_up;
	pcount_dn += f1.pcount_dn;

    }


    public void write(DataOutput out) throws IOException {
	out.writeInt(bcount_up);
	out.writeInt(bcount_dn);
	out.writeInt(pcount_up);
	out.writeInt(pcount_dn);

    }


	public static Layer3Writable read(DataInput in) throws IOException {
	Layer3Writable f = new Layer3Writable();
	f.readFields(in);
	return f;
    }

    public void readFields(DataInput in) throws IOException {
	bcount_up = in.readInt();
	bcount_dn = in.readInt();
	pcount_up = in.readInt();
	pcount_dn = in.readInt();
    }

}

