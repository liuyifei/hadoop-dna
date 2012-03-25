import socket

wildmask = ["255.255.255.255", "127.255.255.255", "63.255.255.255", "31.255.255.255",
           "15.255.255.255", "7.255.255.255", "3.255.255.255", "1.255.255.255",
           "0.255.255.255", "0.127.255.255","0.63.255.255","0.31.255.255",
           "0.15.255.255","0.7.255.255","0.3.255.255","0.1.255.255",
           "0.0.255.255", "0.0.127.255","0.0.63.255", "0.0.31.255",
           "0.0.15.255","0.0.7.255","0.0.3.255","0.0.1.255",
           "0.0.0.255","0.0.0.127","0.0.0.63","0.0.0.31",
           "0.0.0.15","0.0.0.7","0.0.0.3","0.0.0.1",
           "0.0.0.0"]

WILDMASK = {}
for i in range(len(wildmask)):
    WILDMASK[i] = socket.inet_aton(wildmask[i])

subnet = ["255.255.255.255","255.255.255.254","255.255.255.252","255.255.255.248",
        "255.255.255.240","255.255.255.224","255.255.255.192","255.255.255.128",
        "255.255.255.0", "255.255.254.0","255.255.252.0","255.255.248.0",
        "255.255.240.0","255.255.224.0","255.255.192.0","255.255.128.0",
        "255.255.0.0", "255.254.0.0","255.252.0.0", "255.248.0.0",
        "255.240.0.0","255.224.0.0","255.192.0.0","255.128.0.0",
        "255.0.0.0","254.0.0.0","252.0.0.0","248.0.0.0",
        "240.0.0.0","224.0.0.0","192.0.0.0","128.0.0.0",
        "0.0.0.0"]

SUBNET = {}
for i in range(len(subnet)):
    SUBNET[i] = socket.inet_aton(subnet[32-i])

def bitwiseAND(a,b):
    # bitwise a and b
    # bitwise 4 bytes string a,b
    return "%s%s%s%s" % (chr( ord(a[0]) & ord(b[0]) ), chr( ord(a[1]) & ord(b[1]) ), \
                             chr( ord(a[2]) & ord(b[2]) ), chr( ord(a[3]) & ord(b[3]) ) )

def bitwiseOR(a,b):
    # bitwise a and b
    # bitwise 4 bytes string a,b
    return "%s%s%s%s" % (chr( ord(a[0]) | ord(b[0]) ), chr( ord(a[1]) | ord(b[1]) ), \
                             chr( ord(a[2]) | ord(b[2]) ), chr( ord(a[3]) | ord(b[3]) ) )

def toInt(bytes):
    # convert 4 bytes string to integer
    return (ord(bytes[0]) << 24) + (ord(bytes[1]) << 16) + (ord(bytes[2]) << 8) + (ord(bytes[3]))

def IntToDottedIP( intip ):
    octet = ''
    for exp in [3,2,1,0]:
        octet = octet + str(intip / ( 256 ** exp )) + "."
        intip = intip % ( 256 ** exp )
    return(octet.rstrip('.'))

def DottedIPToInt( dotted_ip ):
    exp = 3
    intip = 0
    for quad in dotted_ip.split('.'):
        intip = intip + (int(quad) * (256 ** exp))
        exp = exp - 1
    return(intip)
