#!/bin/sh
javac -classpath "/usr/local/hadoop/hadoop-core-1.0.1.jar":"/usr/local/hadoop/lib/*":"./class" -d class Layer3Writable.java
javac -classpath "/usr/local/hadoop/hadoop-core-1.0.1.jar":"/usr/local/hadoop/lib/*":"./class" -d class Flow.java


jar -cvf hadoop-dna.jar -C class/ .

#/usr/local/src/hadoop-0.20.2/bin/hadoop jar /home/sunshout/flow/flow.jar com.cloud.flow.FlowMR /data/son/temp /data/son/flow
#/usr/local/src/hadoop-0.20.2/bin/hadoop jar /home/sunshout/flow/flow.jar com.cloud.flow.FlowRank /data/son3 /data/son4
