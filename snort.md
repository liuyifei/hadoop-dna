#snort

# Introduction #
snort is


# Installation #
```
apt-get install snort
```

# Alertpkt Format #

```

/* this struct is for the alert socket code.... */
typedef struct _Alertpkt
{
    uint8_t alertmsg[ALERTMSG_LENGTH]; /* variable.. */
    struct pcap_pkthdr pkth;
    uint32_t dlthdr;       /* datalink header offset. (ethernet, etc.. ) */
    uint32_t nethdr;       /* network header offset. (ip etc...) */
    uint32_t transhdr;     /* transport header offset (tcp/udp/icmp ..) */
    uint32_t data;
    uint32_t val;  /* which fields are valid. (NULL could be
                    * valids also) */
    /* Packet struct --> was null */
#define NOPACKET_STRUCT 0x1
    /* no transport headers in packet */
#define NO_TRANSHDR    0x2
    uint8_t pkt[SNAPLEN];
    Unified2EventCommon event;
} Alertpkt;

```