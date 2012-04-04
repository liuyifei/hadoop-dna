#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Author: Choonho Son <choonho.son(at)kt(dot)com>

import zmq
import random
import time
import uuid
import os
context = zmq.Context()

# Socket to send messages on
sender = context.socket(zmq.PUB)
sender.bind("tcp://*:5557")

# Socket with direct access to the sink: used to syncronize start of batch
sink = context.socket(zmq.PUSH)
sink.connect("tcp://cnode16:5558")

#print "Press Enter when the workers are ready: "
#_ = raw_input()
print "Sending tasks to workers"

# The first message is "0" and signals start of batch
uuid = uuid.uuid4()
cmd = "start:%s" % uuid
#1. create hdfs directory
cmd_hdfs = "/usr/local/hadoop/bin/hadoop dfs -mkdir /data/temp/%s" % uuid
os.system(cmd_hdfs)
print cmd
sink.send(cmd)

cmd = "backup:/data/temp/%s" % uuid
print cmd
sender.send(cmd)

# Give 0MQ time to deliver
time.sleep(1)
