# Installation of HBase

# Introduction #
Hbase is colume based database using hadoop.

### Pre-condition ###
  * hadoop is installed in /usr/local/hadoop/
  * jdk is installed in /usr/local/jdk/
  * jookeeper is managed by hbase (you don't need to install zookeeper)

# Installation #
Download Hbase
```
wget http://mirror.apache-kr.org/hbase/stable/hbase-0.92.1.tar.gz
tar zxvf hbase-0.92.1.tar.gz
mv hbase-0.92.1 /usr/local/hbase
```

### hbase-env.sh ###
```
export JAVA_HOME=/usr/local/jdk
export HBASE_CLASSPATH=/usr/local/hbase/conf
```

### hbase-site.xml ###
  * cnode16-m must be changed in your master node's hostname
```

<configuration>
    <property>
         <name>hbase.rootdir</name>
         <value>hdfs://cnode16-m:9000/hbase</value>
    </property>
    <property>
         <name>hbase.master</name>
         <value>cnode16-m:60000</value>
    </property>
    <property>
         <name>hbase.cluster.distributed</name>
         <value>ture</value>
    </property>

    <property>
         <name>hbase.zookeeper.quorum</name>
         <name>cnode16-m</name>
  </property>
</configuration>
```

### regionservers ###
  * add region servers in regionservers file
```
cnode01
cnode02
cnode03
cnode04
cnode05
cnode06
cnode07
cnode08
cnode09
cnode10
cnode11
cnode12
cnode13
cnode14
```

### link hdfs-site.xml ###
```
ln /usr/local/hadoop/conf/hdfs-site.xml /usr/local/hbase/conf/
```

**Copy all these configuration in every Hmaster and HRegionServers**

# start #
  * start master in a HMaster node
```
/usr/local/hbase/bin/start-all.sh
```

  * list process (HQuorumPeer, HMaster}
```
root@cnode16-m:/usr/local/hbase/bin# jps
10634 JobTracker
10293 NameNode
15481 Jps
10523 SecondaryNameNode
14904 HQuorumPeer
14995 HMaster
```

  * In a regionserver {HRegionServer}
```
root@cnode01-m:~# jps
21280 TaskTracker
30156 HRegionServer
21143 DataNode
30246 Jps
```