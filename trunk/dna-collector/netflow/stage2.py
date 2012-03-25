KEY = 0
VALUE = 1

from stage1 import FVALUE

biflow_graph={}

def show():
    keys = biflow_graph.keys()
    keys.sort()
    for key in keys:
        fvs = biflow_graph[key]
        for fv in fvs:
            output = "%s(%s)-%s->(%s)%s" % (key[0],key[1],key[2],key[3],key[4])
            output += " %s %s (%s,%s) (%s,%s) (%s,%s)" % (fv[0],fv[1], (fv[2])[0], (fv[2])[1], (fv[3])[0], (fv[3])[1], (fv[4])[0], (fv[4])[0])
            print output


def biflow_map(flow_indicator, flow_value):
    """
    change to biflow 
    """
    biflow_value = (flow_value[FVALUE.stime], flow_value[FVALUE.etime], (flow_value[FVALUE.bcount], 0), (flow_value[FVALUE.pcount], 0), (flow_value[FVALUE.merge], 0))

    return (flow_indicator, biflow_value)

def biflow_reduce(flow1,flow2):
    """
    flow_value format : stage2 [stime, etime, (b1, b2), (p1, p2), (m1, m2)]
    reduce two flow1 and flow2
    """
    (fi1, fv1) = flow1
    (fi2, fv2) = flow2
    #print "fv1:", fv1
    #print "fv2:", fv2
    # find stime
    if fv1[FVALUE.stime] <= fv2[FVALUE.stime]:
        stime = fv1[FVALUE.stime]
    else:
        stime = fv2[FVALUE.stime]
    # find etime
    if fv1[FVALUE.etime] <= fv2[FVALUE.etime]:
        etime = fv2[FVALUE.etime]
    else:
        etime = fv1[FVALUE.etime]
    fv = (stime, etime, ( (fv1[FVALUE.bcount])[0], (fv2[FVALUE.bcount])[0] ) ,\
              ( (fv1[FVALUE.pcount])[0], (fv2[FVALUE.pcount])[0] ), \
              ( (fv1[FVALUE.merge])[0], (fv2[FVALUE.merge])[0] ) )

    #print "Merge"
    #print fv
    return (fi1, fv)


def flow_reverse(fi):
    """
    @param fi: flow_indicator
    @return : revsersed flow_indicator
    """
    (a,b,c,d,e) = fi
    return (e, d, c, b, a)


def process(fg):
    """
    @param fg : flow graph from stage1
    """
    biflow_graph = {}
    
    keys =fg.keys()
    keys.sort()
    for fi in keys:
        # there are multiple flow_values
        flow_values = fg[fi]
        
        if biflow_graph.has_key(fi) == False:
            rfi1 = flow_reverse(fi)
            if biflow_graph.has_key(rfi1) == False:
                # no flow_indicator
                fvs = []
                for fv in flow_values:
                    (nfi1, nfv1) = biflow_map(fi, fv)
                    fvs.append(nfv1)
                biflow_graph[fi] = fvs
            else:
                # reverse flow_indicator exist
                org_fvs = biflow_graph[rfi1]
                for fv in flow_values:
                    # Real matching (reverse flow2 and flow1s)
                    P2 = (fv[FVALUE.stime], fv[FVALUE.etime])
                    match_book = []
                    for org_fv in org_fvs:
                        #print org_fv
                        P1 = ( org_fv[FVALUE.stime], org_fv[FVALUE.etime] )
                        
                        if (P1[0] <= P2[0]):
                            pctg = intersection(P1, P2)
                        else:
                            pctg = intersection(P2, P1)
                        match_book.append(pctg)

                    max_index = list_max(match_book)
                    flow1 = (rfi1, org_fvs[max_index])
                    flow2 = biflow_map(rfi1, fv)
                    nflow = biflow_reduce(flow1, flow2)
                    #update org_fvs[max_index]
                    org_fvs[max_index] = nflow[VALUE]
        else:
            # flow_indicator exist
            # this is new flow(time shift)
            fvs = biflow_graph[fi]
            for fv in flow_values:
                (nfi1, nfv1) = biflow_map(fi, fv)
                fvs.append(nfv1)

    return biflow_graph


def list_max(mlist):
    max = 0
    index = 0
    max_index = 0
    for value in mlist:
        if max < value:
            value = max
            max_index = index
        index = index+1
    return max_index

def intersection(P1, P2):
    """
    @P1 : (stime1, etime1)
    @P2 : (stime2, etime2)
    find percentage of intersection
    assume : P1 < P2
    """
    (s1, e1) = P1
    (s2, e2) = P2
    if (e1 < s2) : return 0
    else:
        try:
            if e1 <= e2:
                return float(e1 - s2)/float(e1 - s1)
            else:
                return float(e2 - s2)/float(e1 - s1)

        except ZeroDivisionError:
            return 0
