# Build #

apt-get install python-pip
apt-get install python-dev
pip install ncclient


# Basic Usage #


```
<?xml version="1.0" encoding="UTF-8"?><rpc-reply message-id="urn:uuid:df3cb0e2-0af6-11e4-967c-525400784c68">
<lldp-neighbors-information style="brief">
<lldp-neighbor-information>
<lldp-local-interface>xe-0/0/24.0</lldp-local-interface>
<lldp-local-parent-interface-name>-</lldp-local-parent-interface-name>
<lldp-remote-chassis-id-subtype>Mac address</lldp-remote-chassis-id-subtype>
<lldp-remote-chassis-id>00:25:90:e5:62:52</lldp-remote-chassis-id>
<lldp-remote-port-description>p2p1</lldp-remote-port-description>
<lldp-remote-system-name>cnode25-m.testbed.net</lldp-remote-system-name>
</lldp-neighbor-information>
<lldp-neighbor-information>
<lldp-local-interface>xe-0/0/20.0</lldp-local-interface>
<lldp-local-parent-interface-name>-</lldp-local-parent-interface-name>
<lldp-remote-chassis-id-subtype>Mac address</lldp-remote-chassis-id-subtype>
<lldp-remote-chassis-id>00:25:90:e5:62:52</lldp-remote-chassis-id>
<lldp-remote-port-description>p2p2</lldp-remote-port-description>
<lldp-remote-system-name>cnode25-m.testbed.net</lldp-remote-system-name>
</lldp-neighbor-information>
<lldp-neighbor-information>
<lldp-local-interface>me0.0</lldp-local-interface>
<lldp-local-parent-interface-name>-</lldp-local-parent-interface-name>
<lldp-remote-chassis-id-subtype>Mac address</lldp-remote-chassis-id-subtype>
<lldp-remote-chassis-id>00:8e:f2:5a:d9:d2</lldp-remote-chassis-id>
<lldp-remote-port-id-subtype>Locally assigned</lldp-remote-port-id-subtype>
<lldp-remote-port-id>2/g45</lldp-remote-port-id>
</lldp-neighbor-information>
<lldp-neighbor-information>
<lldp-local-interface>xe-0/0/15.0</lldp-local-interface>
<lldp-local-parent-interface-name>-</lldp-local-parent-interface-name>
<lldp-remote-chassis-id-subtype>Mac address</lldp-remote-chassis-id-subtype>
<lldp-remote-chassis-id>90:b1:1c:9f:9e:2d</lldp-remote-chassis-id>
<lldp-remote-port-description>p1p1</lldp-remote-port-description>
<lldp-remote-system-name>gateway-m</lldp-remote-system-name>
</lldp-neighbor-information>
<lldp-neighbor-information>
<lldp-local-interface>xe-0/0/8.0</lldp-local-interface>
<lldp-local-parent-interface-name>-</lldp-local-parent-interface-name>
<lldp-remote-chassis-id-subtype>Mac address</lldp-remote-chassis-id-subtype>
<lldp-remote-chassis-id>90:b1:1c:9f:9e:2d</lldp-remote-chassis-id>
<lldp-remote-port-description>p1p2</lldp-remote-port-description>
<lldp-remote-system-name>gateway-m</lldp-remote-system-name>
</lldp-neighbor-information>
</lldp-neighbors-information>
</rpc-reply>
```