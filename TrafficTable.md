#Traffic Table

# Introduction #

Traffic table stores data which is related with netflow and snort alert.


# Tables #

| Row Key                    | Column Family (bytes)    | Columm Family (packets) | Column Family (alert) |
|:---------------------------|:-------------------------|:------------------------|:----------------------|
| Timestamp_<Monitoring IP>_| B:<dst IP> => nn,mm      | P:<dst IP> => nn,mm     | A:<dst IP> => signature # or contents |
| 1334018704\_10.63.239.236  | B:223.4.119.42 => 181448,107282 | P:223.4.119.42 => 1110,1066 |                       |

for example, we have fllowing netflow data:

_10.63.239.236\_223.4.119.42      181448 107282 1110 1066_

| monitoring IP  | 10.63.239.236 |
|:---------------|:--------------|
| destination IP | 223.4.119.42  |
| sent bytes     | 181448        |
| receive bytes  | 107282        |
| sent packets   | 1110          |
| receive packets| 1066          |