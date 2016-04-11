

mgmt is management system for install hardware/OS

Base OS : CentOS 6.x (64bit)

# Introduction #

boot
dhcp
dns


# dhcp #

dhcp is dhcp daemon for allow dhcp IP distribution for Data Node and Name Node

### installation ###

```
yum install dhcp
chkconfig dhcpd on
```

### edit configuration ###

edit /etc/dhcp/dhcpd.conf

```
include "/etc/dhcp/dhcpd.pod";
```

make dhcp information (/etc/dhcp/dhcpd.pod)

```
subnet 10.7.1.0 netmask 255.255.255.192 {
authoritative;
option domain-name-servers 8.8.8.8;
option routers 10.7.1.62;
next-server 10.7.1.22;
}


group {
     host cnode01 {
        hardware ethernet 60:eb:69:db:fc:9e;
        fixed-address 10.7.1.1;
        option host-name "cnode01-m.hadoop-dna.org";
        filename "pxelinux.0";
     }

     host cnode02 {
        hardware ethernet 60:eb:69:db:fd:06;
        fixed-address 10.7.1.2;
        option host-name "cnode02-m.hadoop-dna.org";
        filename "pxelinux.0";
     }
```

# tftp-server #

tftp server works as repository for net installation media

### installation ###

```
yum install tftp-server

```

default tftp directory : /var/lib/tftpboot/

### net boot media ###

```
default auto
label auto
        menu label ^Automated install
        kernel ubuntu-installer/amd64/linux
        append auto=true priority=critical vga=normal initrd=ubuntu-installer/amd64/initrd.gz url=http://10.7.1.22/cnode.cfg netcfg/choose_interface=eth0 -- quiet
```

# apache #

### installation ###

```
yum install httpd
```