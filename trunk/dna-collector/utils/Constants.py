'''
Created on 2011. 5. 5.

@author: Son
'''

from os.path import exists,join
 
##############################
# TODO: specify project name
##############################
PRJ_NAME = "dna-collector"

# base dir
BASE_DIR                    = '/usr/local/%s' % PRJ_NAME
CONF_DIR                    = join(BASE_DIR, "conf")
BIN_DIR                     = join(BASE_DIR, "bin")

# base file
CONF_FILE                   = join(CONF_DIR, "%s.ini" % PRJ_NAME)

#runtime dir
PID_DIR                     = '/var/run/'
SHUTDOWN_FLAG               = "%s/%s.shutdown" % (PID_DIR, PRJ_NAME)
AGENT_SHUTDOWN_MODE_FLAG    = "%s/shutdown_mode" % PID_DIR
LOG_DIR                     = '%s/var/log/' % PRJ_NAME
