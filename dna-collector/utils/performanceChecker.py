import time

def elapsed_time(func):
    # func is a function object after annotation
    def decorated(*args, **xargs):
        start = time.time()
        func(args, xargs)
        end = time.time()
        print "[%s] Elapse time: %5f" % ( func.__name__, (end-start) )
    return decorated

