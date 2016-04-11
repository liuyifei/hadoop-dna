#Describe netflow format

# Netflow V5 #

## Header ##

| Bytes | Contents | Description |
|:------|:---------|:------------|
| 0-1   | version  | NetFlow export format version number |
| 2-3   | count    | Number of flows exported in this packet (1-30) |
| 4-7   | SysUptime | Current time in milliseconds since the export device booted |
| 8-11  |unix\_secs|Current count of seconds since 0000 UTC 1970|
|12-15  |unix\_nsecs|Residual nanoseconds since 0000 UTC 1970|
|16-19  |flow\_sequence|Sequence counter of total flows seen|
|20     |engine\_type|Type of flow-switching engine|
|21     |engine\_id|Slot number of the flow-switching engine|
|22-23  |sampling\_interval|First two bits hold the sampling mode; remaining 14 bits hold value of sampling interval|

## Record ##