import sys
import socket

KEY = 0
VALUE = 1

class FLOW:
    link = 0
    sip = 1
    dip = 2
    pcount = 3
    bcount = 4
    stime = 5
    elapse = 6
    sport = 7
    dport = 8
    proto = 9

class FVALUE:
    stime = 0
    etime = 1
    bcount = 2
    pcount = 3
    merge = 4

TIMEOUT_INTERVAL = 7200   #second

###############################
# flow graph : dictionary
# key: flow_indicator
# value: [(stime, value) ...]
# flow_indicator : [(stime,(etime, bcount, pcount, merge)) ......]
###############################
flow_graph = {}

def show():
    keys = flow_graph.keys()
    keys.sort()
    for key in keys:
        flow_values = flow_graph[key]
        for flow_value in flow_values:
            output = "%s(%s)-%s->(%s)%s" % (key[0],key[1],key[2],key[3],key[4])
            (stime, etime, bcount, pcount, merge) = flow_value
            output += " | %s->%s Bytes(%s), Count(%s) merge(%s)" % \
                (stime, etime, bcount, pcount, merge)
            print output

################################################
# definition : flow
# key : value
# key => flow_indicator (sip, sport, proto, dport, dip)
# value = flow_value (stime, etime, bcount, pcount, # of flow)
################################################
def flow_map(netflow, delim="|"):
    """
    @param: single netflow 
    @return map element pair (key, value)
    netflow : link, sip, dip, pcount, bcount, stime, elapse, sport, dport, proto
    @notice: netflow does not have carriage return 
    """
    item = netflow.split(delim)
    # KEY
    flow_indicator = ( item[FLOW.sip], \
                          int(item[FLOW.sport]), \
                          int(item[FLOW.proto]), \
                          int(item[FLOW.dport]), \
                           item[FLOW.dip] )

    # VALUE
    stime = float(item[FLOW.stime])
    etime = float(item[FLOW.stime]) + float(item[FLOW.elapse])/1000
    bcount = int(item[FLOW.bcount])
    pcount = int(item[FLOW.pcount])
    merge = 1
    flow_value = (stime, etime, bcount, pcount, merge)

    # return new flow
    return (flow_indicator, flow_value)

def flow_map2(link):
    """
    @param: link object in timeline(Datastructure)
    @return map element pair (key,value)
          0      1       2      3      4      5      6         7       8 
    link: stime, elapse, saddr, daddr, sport, dport, protocol, pcount, bcount
    """
    # KEY
    flow_indicator = ( socket.inet_ntoa(link[2]), \
                           link[4], link[6], link[5], \
                           socket.inet_ntoa(link[3]) )
    # VALUE
    flow_value = (link[0], float(link[0]) + float(link[1])/1000, link[8], link[7], 1)
    # return new flow
    return (flow_indicator, flow_value)
                           
    

def flow_reduce(flow1, flow2):
    """
    @param : flow1, flow2
    @return : new flow1
    flow1 and flow2 have same flow_indicator
    but, different stime, etime, bcount, pcount, merge
    merge into new flow1 starting flow1 and ending flow2
    """
    (stime1, etime1, bcount1, pcount1, merge1) = flow1[VALUE]
    (stime2, etime2, bcount2, pcount2, merge2) = flow2[VALUE]

    #reduce two flows
    new_flow_value = (stime1, etime2, bcount1+bcount2, pcount1+pcount2, merge1+merge2)

    # return reduced flow
    return (flow1[KEY], new_flow_value)


def process_datastrucure(links):
    """
    read from datastructure
    make new netflow with map/reduce
    @param links : uplink or dnlink in timeline
    """
    #clear previous garbage
    flow_graph = {}

    for line in links:
        (flow_indicator2, flow_value2) = flow_map2(line)
        if flow_graph.has_key(flow_indicator2) == False:
            # add new flow
            flow_graph[flow_indicator2] = [ flow_value2 ]

        else:
            # flow indicator already exist
            # check reducable
            MATCHED = False
            flow_values = flow_graph[flow_indicator2]
            num_index = len(flow_values)
            for index in range(num_index):
                # reverse matching for performance
                flow_value1 = flow_values[-1 - index]
                if ( flow_value2[FVALUE.stime] >= (flow_value1[FVALUE.etime] - TIMEOUT_INTERVAL) ) and \
                        (flow_value2[FVALUE.stime] <= (flow_value1[FVALUE.etime] + TIMEOUT_INTERVAL) ):
                    # reducable
                    new_flow = flow_reduce( (flow_indicator2, flow_value1), (flow_indicator2, flow_value2) )
                    # update flow_graph
                    flow_values[-1 - index] = new_flow[VALUE]
                    MATCHED = True
                    break

            # no match
            if MATCHED == False:
                flow_values.append( flow_value2 )

    return flow_graph

def process_file(fname):
    """
    read netflow file
    make new netflow with map/reduce
    """
    #clear previous garbage
    flow_graph = {}

    fp = open(fname, "r")
    for line in fp:
        temp = line.split("\n")
        (flow_indicator2, flow_value2) = flow_map(line)
        if flow_graph.has_key(flow_indicator2) == False:
            # add new flow
            flow_graph[flow_indicator2] = [ flow_value2 ]

        else:
            # flow indicator already exist
            # check reducable
            MATCHED = False
            flow_values = flow_graph[flow_indicator2]
            num_index = len(flow_values)
            for index in range(num_index):
                # reverse matching for performance
                flow_value1 = flow_values[-1 - index]
                if ( flow_value2[FVALUE.stime] >= (flow_value1[FVALUE.etime] - TIMEOUT_INTERVAL) ) and \
                        (flow_value2[FVALUE.stime] <= (flow_value1[FVALUE.etime] + TIMEOUT_INTERVAL) ):
                    # reducable
                    new_flow = flow_reduce( (flow_indicator2, flow_value1), (flow_indicator2, flow_value2) )
                    # update flow_graph
                    flow_values[-1 - index] = new_flow[VALUE]
                    MATCHED = True
                    break

            # no match
            if MATCHED == False: 
                flow_values.append( flow_value2 )


if __name__ == "__main__":
    flow_graph = process(sys.argv[1])
    import stage2
    stage2.process(flow_graph)
    print stage2.show()

