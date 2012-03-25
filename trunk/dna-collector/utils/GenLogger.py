import logging
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
import sys
from os.path import join

LOG_LEVELS = {'debug'       :logging.DEBUG,\
              'info'    :logging.INFO, \
              'warning' : logging.WARNING, \
              'error'   : logging.ERROR, \
              'critical': logging.CRITICAL }


def getLogger(config, section, keyword="Test", tid=None):
    """
    @param config : ConfigParser object
    @param section : Section in config
    @param keyword : additional keyword
    """

    level = config.get("global","log_level")

    log_dir = config.get("global", "log_dir")
    log_path = config.get(section, "logfile")
    fname = join(log_dir, log_path)

    #Thread id(Multiprocess id)
    if tid != None:
        fname = "%s.%s" % (fname,tid)

    logger = logging.getLogger(str(keyword))              
    logger.setLevel( LOG_LEVELS[level] )

    if fname:
        log_handler = RotatingFileHandler(fname, maxBytes=100000000, backupCount=5)
    else:
        log_handler = StreamHandler(sys.stdout)

    log_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    log_handler.setFormatter(log_formatter)
    logger.addHandler(log_handler)

    return logger
