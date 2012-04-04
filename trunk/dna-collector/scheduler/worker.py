#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Task worker
#
# Author: Choonho Son <choonho.son(at)kt(dot)com>

import sys
import time
import zmq
import socket
import os

def merge_files(src, dst):
    files = os.listdir(src)
    hostname = socket.gethostname()
    for file in files:
        created = file.split("_")
        full_path = os.path.join(src, file)
        t = time.localtime(float(created[0]))
        fname = "%4d-%.2d-%.2d-%.2d.%s" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, hostname)

        src_fp = os.stat(full_path)
        if src_fp.st_mode != 33060: #r__r__r
            #may be writing from collector
            continue

        new_fp = os.path.join(dst, fname)
        fp = open(new_fp, 'a')
        fp.write(open(full_path).read())
        fp.close()

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.SUB)
receiver.connect("tcp://cnode16:5557")
filter = "backup"
receiver.setsockopt(zmq.SUBSCRIBE, filter)
# Socket to send messages to
sender = context.socket(zmq.PUSH)
sender.connect("tcp://cnode16:5558")

hostname = socket.gethostname()
# Process tasks forever
while True:
    print "ready to receive"
    cmd = receiver.recv()
    temp = cmd.split(":")

    print "dir:", temp[1]
    temp_dir = os.path.join("/data/temp",temp[1])
    start_cmd = "%s:start" % hostname
    sender.send(start_cmd)
    # Do the work
    os.mkdir(temp_dir)
    merge_files("/data/netflow",temp_dir)

    end_cmd = "%s:finished" % hostname
    # Send results to sink
    sender.send(end_cmd)
