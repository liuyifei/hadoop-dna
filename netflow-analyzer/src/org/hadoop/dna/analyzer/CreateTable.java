package org.hadoop.dna.analyzer;

import java.io.IOException;

import org.apache.hadoop.conf.*;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.hbase.HBaseConfiguration;
import org.apache.hadoop.hbase.HColumnDescriptor;
import org.apache.hadoop.hbase.HTableDescriptor;
import org.apache.hadoop.hbase.client.HBaseAdmin;

public class CreateTable {

	/**
	 * @param args
	 */
	public static void main(String[] args) throws IOException {
		// 1. create table
		// 2. create column family
		// ref: http://code.google.com/p/hadoop-dna/wiki/TrafficTable
		HTableDescriptor descriptor = new HTableDescriptor("Traffic");
		descriptor.addFamily(new HColumnDescriptor("B"));  //bytes 
		descriptor.addFamily(new HColumnDescriptor("P"));  //packets
		descriptor.addFamily(new HColumnDescriptor("A"));  //alerts
		
		try {
			Configuration config = HBaseConfiguration.create();
			config.addResource(new Path("/usr/local/hbase/conf/hbase-default.xml"));
			config.addResource(new Path("/usr/local/hbase/conf/hbase-site.xml"));
			HBaseAdmin admin = new HBaseAdmin(config);
			// Create Table
			admin.createTable(descriptor);
			System.out.println("Table Created...");
		} catch (IOException e) {
			System.out.println("IOExeption: cannot create table");
			e.printStackTrace();
		}
	}
}
