'''
Created on 2011. 5. 5.

@author: Son (chonho@kt.com)
@copyright: GPL
'''

import socket
import time
from os.path import basename, exists
from os import mkdir
from optparse import OptionParser
from ConfigParser import ConfigParser
from multiprocessing import Process, Queue


from utils.Daemon import daemonize
from utils.GenLogger import getLogger
from utils.Debug import *
import utils.Constants as Constants

# server
from server.collector import netflowCollector
from server.analyzer  import netflowAnalyzer

def start(config):
    """
    start multiprocess
    """
    netflow_queue = Queue()


    processInfo("main")
    ##############
    # Collector
    #############
    collector = Process(target=netflowCollector, args=(config, netflow_queue) )

    ############
    # Analyzer
    ############
    num_of_analyzers = config.getint("analyzer","num_of_analyzers")
    analyzers = []
    for index in range(num_of_analyzers):
        analyzers.append( Process(target=netflowAnalyzer,  args=(config, netflow_queue)) )

    # Start (analyzer, collector)
    for analyzer in analyzers:
        analyzer.start()
    collector.start()
    
    # join 
    collector.join()
    for analyzer in analyzers:
        analyzer.join()


def main():
    
    # TODO: Option Parser
    parser = OptionParser()
    parser.add_option("-f", "--file", dest="filename", help="configuration file(default:skeleton.ini)")
    parser.add_option("-d", "--daemon", dest="daemon", action="store_true", help="run as background daemon")
    parser.add_option("-w", "--web", dest="web", help="Web API Server")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true")
    
    (options, args) = parser.parse_args()
    
    # Config Parser
    conf = Constants.CONF_FILE
    if options.filename:
        conf = options.filename
    config = ConfigParser()

    print conf
    config.read(conf)
    
    # pre-condition
    # log directory
    hostname = socket.gethostname()
    running = config.get("global",hostname)
    if running == "off": return

    log_dir = config.get("global","log_dir")
    if exists(log_dir) == False:
        mkdir(log_dir)

    # Check daemonize
    pid_filename = basename(__file__).split(".")[0]
    if options.daemon:
        config.set("global","daemon",True)
        daemonize(pid_filename)
    
    # TODO: Call main procedure
    start(config)
    
if __name__ == '__main__':
    main()
    
