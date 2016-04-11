# Analysis of 10G NIC driver.

# Introduction #

```
struct ixgbe_ring {
    struct ixgbe_ring *next;    /* pointer to next ring in q_vector */
    struct ixgbe_q_vector *q_vector; /* backpointer to host q_vector */
    struct net_device *netdev;  /* netdev ring belongs to */
    struct device *dev;     /* device for DMA mapping */
    void *desc;         /* descriptor ring memory */
    union {
        struct ixgbe_tx_buffer *tx_buffer_info;
        struct ixgbe_rx_buffer *rx_buffer_info;
    };
    unsigned long state;
#ifndef NO_LER_WRITE_CHECKS
    u8 __iomem **adapter_present;   /* Points to field in ixgbe_hw */
#endif /* NO_LER_WRITE_CHECKS */
    u8 __iomem *tail;
    dma_addr_t dma;         /* phys. address of descriptor ring */
    unsigned int size;      /* length in bytes */

    u16 count;          /* amount of descriptors */

    u8 queue_index; /* needed for multiqueue queue management */
    u8 reg_idx;         /* holds the special value that gets
                     * the hardware register offset
                     * associated with this ring, which is
                     * different for DCB and RSS modes
                     */
    u16 next_to_use;
    u16 next_to_clean;

#ifdef HAVE_PTP_1588_CLOCK
    unsigned long last_rx_timestamp;

#endif
    union {
#ifdef CONFIG_IXGBE_DISABLE_PACKET_SPLIT
        u16 rx_buf_len;
#else
        u16 next_to_alloc;
#endif
        struct {
            u8 atr_sample_rate;
            u8 atr_count;
        };
    };

    u8 dcb_tc;
    struct ixgbe_queue_stats stats;
#ifdef HAVE_NDO_GET_STATS64
    struct u64_stats_sync syncp;
#endif
    union {
        struct ixgbe_tx_queue_stats tx_stats;
        struct ixgbe_rx_queue_stats rx_stats;
    };
} ____cacheline_internodealigned_in_smp;

```

# Details #

Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages