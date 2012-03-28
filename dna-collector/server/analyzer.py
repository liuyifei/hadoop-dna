#from threading import Thread
import socket
import struct
import time
import re
import stat
import os
from os.path import join

from utils.Debug import *
from utils.GenLogger import getLogger
from netflow.addr import *

logger = None

totalCount = 0
totalFlow = 0 
pid = -1

class NetflowAnalyzer:

    def __init__(self, config, flow_queue):
        self.config = config
        self.flow_queue = flow_queue
        self.interval = config.getint("backup","interval")

    def start(self):
        global totalCount
        global totalFlow
        global pid

        send = ""
        sendCount = 0          # current count in send
        curr = time.time()     # time difference after privous sent
        priv = curr 

        while 1:
            data = self.flow_queue.get()
            # count received Netflow Data
            totalCount += 1

            (header, records) = self.parseNetflow5Packet(data)
            sut = header['SysUpTime']
            es  = header['EpochSeconds']
            # 48 : size of Netflow Record
            for index in range(len(records) / 48):
                start = index * 48
                record = records[start:start+48]
                #d = flow
                d = self.parseRecord(record)
                #get start time of flow (based on collector's time)
  
                stime = d['stime']
                milisecond = stime - sut
                elapse_second = milisecond / 1000
                (sec, mili) = (es + elapse_second, milisecond % 1000) 
                my_stime = "%s.%s" % (sec, mili)
                result = "%s %d %d %s %d %s %s %d %d" % (\
                    socket.inet_ntoa(d['saddr']), d['sport'], d['protocol'], socket.inet_ntoa(d['daddr']), d['dport'],
                    my_stime, d['etime']-stime, d['pcount'], d['bcount'])

                send = send + result + "\n"
                # count processed Neflow Records
                totalFlow += 1


            # check for send
            curr = time.time()
            if (curr - priv) > self.interval: #every 60 seconds 
                # send data to queue
                who = "%s_%s" % (str(curr), str(pid))
                fname = join(self.config.get("backup","path"), who)
                logger.debug("==================================================")
                logger.debug("Total Count\tTotal Flow\t File, Current Count")
                logger.debug("%s\t%s\t%s\t%s" % (totalCount,totalFlow,fname,len(send)))
                fp = open(fname,'w')
                # clear send information
                fp.write(send)
                fp.close()
                # change mode to read only
                os.chmod(fname,stat.S_IRUSR|stat.S_IRGRP|stat.S_IROTH)

                send = ""
                priv = curr

            #print "[%d] %d %d" % (pid, totalCount, totalFlow)

    def parseNetflow5Packet(self, packet):
        # parse to Header , Records
        header = {}
        header['SysUpTime'] = socket.ntohl(struct.unpack('I',packet[4:8])[0])
        # fix time to localtime zone
        #header['EpochSeconds'] = socket.ntohl(struct.unpack('I',packet[8:12])[0]) - (time.timezone)
        header['EpochSeconds'] = socket.ntohl(struct.unpack('I',packet[8:12])[0])
        
        # 24 : size of Netflow Header
        return (header,packet[24:])

    def parseRecord(self, record):
        # record is netflow v5 header
        # return flow_t dictionary
        d = {}
        d['saddr'] = record[0:4]
        d['daddr'] = record[4:8]
        d['pcount'] = socket.ntohl(struct.unpack('I',record[16:20])[0])
        d['bcount'] = socket.ntohl(struct.unpack('I',record[20:24])[0])
        d['stime'] = socket.ntohl(struct.unpack('I',record[24:28])[0])
        d['etime'] = socket.ntohl(struct.unpack('I',record[28:32])[0])
        d['sport'] = socket.ntohs(struct.unpack('H',record[32:34])[0])
        d['dport'] = socket.ntohs(struct.unpack('H',record[34:36])[0])
        d['protocol'] = ord(record[38])
        """
        return "%s %d %d %s %d %s %s, %d %d" % ( \
            socket.inet_ntoa(d['saddr']), d['sport'], \
                d['protocol'], socket.inet_ntoa(d['daddr']), d['dport'], \
                d['stime'], d['etime'], d['pcount'], d['bcount'])
        #debug(result, "Record")
        #logging.debug(result)
        """
        return d


    def toString(self, d):
        """
        @param d : record dictionary
        @return : human readable flow 
        """
        result = "%s(%d) -(%d)-> %s(%d) from %s to %s, pcount:%d, bcount:%d" % (
            socket.inet_ntoa(d['saddr']), d['sport'], d['protocol'], socket.inet_ntoa(d['daddr']), d['dport'],
            d['stime'], d['etime'], d['pcount'], d['bcount'])
        return result

            
def netflowAnalyzer(config, flow_queue):
    global logger
    global pid
    pid = processInfo("netflowAnalyzer")
    
    logger = getLogger(config, "analyzer", pid, pid)
    logger.info("Start netflow Analyzer(PID: %s)" % pid)
    
    #global queue_netflow
    #global queue_db
    #queue_netflow = flow_queue
    myinstance = NetflowAnalyzer(config, flow_queue)
    myinstance.start()
    logger.debug("Netflow Analyzer Received Counter: %s" % totalCount)
