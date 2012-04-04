#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Collects results from workers via that socket
#
# Project: hadoop-dna (dna-collector)
# Author: Choonho Son <choonho.son(at)kt(dot)com>

import sys
import time
import zmq
import logging

context = zmq.Context()
logging.basicConfig(filename='/var/log/sink.log', level=logging.DEBUG)

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

def is_finished(workers):
    print workers
    keys = workers.keys()
    finished = True
    for key in keys:
        if workers[key] == "start":
            finished = False
    return finished

def parse_cmd(cmds):
    """
    <hostname>:start
    <hostname>:finished
    """
    cmd = cmds.split(":")
    return (cmd[0], cmd[1])

workers={}
while True:
    s = receiver.recv()
    if s == "start":
        logging.debug("Start...")
        workers = {}
    else:
        (who, cmd) = parse_cmd(s)
        workers[who] = cmd
        if is_finished(workers) == True:
            logging.debug("Finished...")
            print "Finalized workers"
            workers = {}

# Calculate and report duration of batch
tend = time.time()
print "Total elapsed time: %d msec" % ((tend-tstart)*1000)
