#Convert netflow data into graph representation

# Introduction #

convert netflow to graph representation.
This is bigraph between IPs which does not show traffic volumes.

# Data Format #
## Input data ##

  * input data is number of lines like:

```
10.63.215.226 80 6 192.209.113.100 1656 1346857155.998 2683 35 73916
10.63.218.76 22122 6 192.107.167.142 38858 1346857159.297 8 4 268
10.63.217.88 80 6 192.38.112.83 9747 1346857160.218 2065 4 426
10.63.224.132 5223 6 192.36.132.23 1804 1346857162.780 0 1 221
10.63.217.112 47792 6 192.187.171.216 22 1346857173.174 445 12 1152
10.63.225.200 5223 6 192.168.33.197 59418 1346857179.65 0 1 95
...
```

**format**

```
Src IP, Src Port, Protocol, Dst IP, Dst Port, Start Time(timestamp), Elapse(ms), Bytes, Packets
```

## Output data ##

  * output data is graph key, value representation

```
10.63.215.226 192.209.113.100 192.42.5.3 14.4.6.2 8.8.8.8 ...
192.209.113.100 10.63.215.226 8.8.8.8 ...
...
```

Line #1 shows that
Source IP(10.63.215.226) sent packets to Destination IPs(192.209.113.100 192.42.5.3 14.4.6.2 8.8.8.8)

Src IP, list of Dst IPs

# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages