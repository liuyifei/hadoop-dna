'''
Created on 2011. 5. 13.

@author: Son
'''
from os.path import basename, join
import SocketServer
import socket
import logging
import struct

from utils.Debug import *
from utils.GenLogger import getLogger

logger = None
queue_netflow = None

totalCount = 0
recvCount = 0

class NetflowCollector(SocketServer.BaseRequestHandler):
    """
    Netflow Collector
    1) Listen UDP packet,
    2) Push to Queue, if it is netflow 5
    """

    def __init__(self, request, client_address, server):
        self.recvCount = 0
        SocketServer.BaseRequestHandler.__init__(self, request, client_address, server)

    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]

        # counter
        global totalCount
        global recvCount
        totalCount += 1
        
        #print "[%d]data:[%s]" % (totalCount, data)
        #socket.sendto(data.upper(), self.client_address)

        # Check Packet is netflow v5
        (TF, version) = self.checkNetflowPacket(data)

        if TF:
            queue_netflow.put(data)
            recvCount = recvCount + 1
        else:
            #logger.error("Received Wrong Netflow Record from %s" % self.client_address[0])
            #logger.error("Data:[%s]" % data)
            pass

        #logger.info("count:%d" % totalCount)

    def checkNetflowPacket(self, packet):
        # Check packet is Netflow v5
        # return (TF, records)
        version = socket.ntohs(struct.unpack('H',packet[0:2])[0])
        count = socket.ntohs(struct.unpack('H',packet[2:4])[0])
        #print "Version", version, "count", count
        if version == 5 and (count*48 + 24) == len(packet):
            # correct netflow 5
            return (True, 5)
        return (False, -1)
    

def netflowCollector(config, queue):
    """
    @param: config , global configuration variable
    """

    global logger
    global queue_netflow
    
    pid = processInfo("netflowCollector")
    port = config.getint("collector","port")
    logger = getLogger(config, "collector", pid)

    queue_netflow = queue
    logger.info("Start netflow Collector(PID: %s)" % pid)
    logger.info("Netflow Listen port : %s" % port)
    myserver = SocketServer.UDPServer(("127.0.0.1",port),NetflowCollector)
    myserver.serve_forever()

if __name__ == "__main__":
    print "Test NetflowCollector"
