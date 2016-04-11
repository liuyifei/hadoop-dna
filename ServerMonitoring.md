#server monitoring using SNMP + zenoss

# Introduction #
SNMP is simple network monitoring protocol.
Zenoss is open source monitoring tool.

```
# wget --no-check-certificate https://raw.github.com/zenoss/core-autodeploy/master/core-autodeploy-4.2.sh
# chmod +x core-autodeploy-4.2.sh
# ./core-autodeploy-4.2.sh
```

# Installation #
SNMP Installation in Ubuntu.
SNMP must be installed in every monitored devices.

```
apt-get install snmpd
```

# Configure #
edit /etc/snmp/snmpd.conf
```
rocommunity public
syslocation cnode-m
syscontact choonho.son@kt.com
```

edit /etc/default/snmpd
  1. insert config file like -c /etc/snmp/snmpd.conf
```
# snmpd options (use syslog, close stdin/out/err).
#SNMPDOPTS='-Lsd -Lf /dev/null -u snmp -g snmp -I -smux -p /var/run/snmpd.pid'
SNMPDOPTS='-Lsd -Lf /dev/null -u snmp -g snmp -I -smux -p /var/run/snmpd.pid -c /etc/snmp/snmpd.conf'
```