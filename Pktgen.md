#Pktgen is a traffic generator powered by Intel's DPDK at 10Gbit wire rate traffic with 64 byte frames.

# Introduction #

Add your content here.


# Installation #

1. Download Pktgen-DPDK from git
```
git clone git://github.com/Pktgen/Pktgen-DPDK.git
```

2. Build dpdk of Pktgen-DPDK
```
cd Pktgen-DPDK/dpdk
export RTE_SDK=${installDir}/Pktgen-dpdk/dpdk
export RTE_TARGET=x86_64-wr-linuxapp-gcc
make install T=x86_64-wr-linuxapp-gcc
```

3. Build Pktgen example
```
cd Pktgen-DPDK/dpdk/wr-examples/pktgen
export RTE_SDK=${installDir}Pktgen-dpdk/dpdk
make
```

4. running pktgen
```
sudo ./app/build/pktgen -c 0xe0 -n 4 -- p 0xf0 -m "6.0.7.1"
```

# References #
  * https://github.com/Pktgen/Pktgen-DPDK