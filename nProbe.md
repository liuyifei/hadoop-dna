# execute nProbe for collecting netflow data

# Installation #
```
wget http://hadoop-dna.googlecode.com/files/nProbe-4.9.4.tar.gz
tar -zxvf nProbe-4.9.4.tar.gz
cd nProbe
./autogen.sh
make
make install
```
To compile nProbe, libtool, autoconf, automake, libpcap-dev are needed.

# Update start script #

ubuntu start script

```
root@cnode01-m:/etc/init.d# update-rc.d  nprobe defaults
 Adding system startup for /etc/init.d/nprobe ...
   /etc/rc0.d/K20nprobe -> ../init.d/nprobe
   /etc/rc1.d/K20nprobe -> ../init.d/nprobe
   /etc/rc6.d/K20nprobe -> ../init.d/nprobe
   /etc/rc2.d/S20nprobe -> ../init.d/nprobe
   /etc/rc3.d/S20nprobe -> ../init.d/nprobe
   /etc/rc4.d/S20nprobe -> ../init.d/nprobe
   /etc/rc5.d/S20nprobe -> ../init.d/nprobe
```

# Output Format #
```
14.63.215.226 80 6 49.1.21.74 4800 1332676559.441 203 25 77082
```
  1. Src IP    : (ex. 14.63.215.226)
  1. Src Port  : (ex. 80)
  1. Protocol  : (ex. 6) 6 TCP, 17 UDP ...
  1. Dst IP    : (ex. 49.1.21.74)
  1. Dst Port  : (ex. 4800)
  1. Start Time : (ex. 1332676559.441 epoch second)
  1. Duration   : (ex. 203 mili second)
  1. Number of packets : (ex. 25 packets)
  1. Number of bytes : (ex. 77082 bytes)