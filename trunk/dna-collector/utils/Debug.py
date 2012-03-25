import os

def processInfo(title=None):
    print "name      : ", title
    print "Parent pid: ", os.getppid()
    print "pid       : ", os.getpid()
    return os.getpid()
