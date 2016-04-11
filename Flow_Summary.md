# Flow Summary

# Introduction #

## Layer3Flow ##
> This summarizes network flow based on source IP and destination IP

> Usage)
```
 hadoop jar hadoop-dna.jar org.hadoop.dna.analyzer.Layer3Sum 2012-07-14-22-15
```

> Result looks like

| Row key | src IP dst IP , ex) 14.6.1.34\_8.8.8.8 |
|:--------|:---------------------------------------|
| Data    | Bytes Sent, Bytes Receive, Packet Sent, Packet Receive |

14.6.1.34.23\_8.8.8.8   10445 3423 53 24

## Layer3Flow2 ##

This summarizes network flow based on monitoring IP
It is summation of multiple destination IPs.

> Usage)
```
 hadoop jar hadoop-dna.jar org.hadoop.dna.analyzer.Layer3Sum2 2012-07-14-22-15
```

> Result looks like

| Row key | monitoring IP , ex) 14.6.1.34 |
|:--------|:------------------------------|
| Data    | Bytes Sent, Bytes Receive, Packet Sent, Packet Receive |

14.6.1.34   10445 3423 53 24

## Layer3Graph ##

Layer3Graph makes Digraph of flow, which is used for FlowRank algorithm.

| Input Path |   /data/temp/  |
|:-----------|:---------------|
| Output Path  | /data/graph\_out/   |

> Usage)
```
 hadoop jar hadoop-dna.jar org.hadoop.dna.analyzer.Layer3Graph 2012-07-14-22-15
```

## FlowRank ##

FlowRank is the PageRank algorithm for Netflow Flow

| Input Path | Output of Layer3Graph |
|:-----------|:----------------------|
| Output Path | User defined folder   |


> Usage)
```
 hama jar hama-examples-0.5.0.jar pagerank <Input Path> <Output Path>
```