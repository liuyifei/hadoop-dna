# Traffic Analysis Format #

## Introduction ##

Traffic analysis format can be categorized on OSI 7 Layer.

## Key Format ##

### Layer 4 Format ###

Input Format  :
```
<Src IP> : <Src Port> : <Protocol> : <Dst Port> : <Dst IP>
```

ex) 192.168.0.1:1234:7:80:10.1.2.3

```
public class Layer4Writable implements WritableComparable {
   //field
   private Text srcIP;
   private Int srcPort;
   private Int proto;
   private Int dstPort;
   private Text dstIP;
}

```

### Layer 3 Format ###

Input Format :
```
<Src IP> - <Dst IP>
```

ex)192.168.0.1:10.1.2.3

```
public class Layer4Writable implements WritableComparable {
   //field
   private Text srcIP;
   private Text dstIP;
}

```

# Details #


Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages