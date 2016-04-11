## Hadoop based, a Distributed Network Analyzer ##

### Abstract ###

DNA is a large scale network analysis framework based on Hadoop DFS and Hama BSP that allows you to mine and analyze the large network traffic.

Problems:

![http://hadoop-dna.googlecode.com/files/download_18G.png](http://hadoop-dna.googlecode.com/files/download_18G.png)

How to monitor:

![http://hadoop-dna.googlecode.com/files/Hadoop-DNA.png](http://hadoop-dna.googlecode.com/files/Hadoop-DNA.png)

### Proposal ###
![https://hadoop-dna.googlecode.com/svn/wiki/dna_framework.png](https://hadoop-dna.googlecode.com/svn/wiki/dna_framework.png)

### Background ###

### Rationale ###

### Initial Goal ###

  * Multiple Giga bytes realtime traffic monitoring
  * Netflow traffic statistics based on Map/Reduce
  * Flow Ranking based on hama
  * Anomaly detection based on machine learning
  * Intrusion detection based on GPU

### External Dependencies ###

  * DPDK http://dpdk.org/
  * DPDK-Netflow https://code.google.com/p/netflow-dpdk/
  * Apache Hadoop
  * Apache HBase
  * Apache Hama

### Initial Committers ###

  * Choonho Son <choonho.son@gmail.com>
  * Edward J. Yoon <edwardyoon@apache.org>

### Google Group ###
https://groups.google.com/forum/#!forum/hadoop-dna