# Lecture 5 - Application Layer Continued
### IP address and port number
- IPV4
  - 127.0.0.1
  - 32 Bit
- L4 Is the process to process layer
Take this example system:
PC - ROUTER - INTERNET - ROUTER - SERVER
- On server side, there must be a process which has a socket
- On the OS kernel side there should be a TCP layer and below that an IP layer and which there is a driver below that
  - L1 and L2 is somewhere between the NIC and the Drivers
  - TCP IP is where the L3 and L4 live
#### To connect to a Google server

1.  www.google.com
2.  TCP connection - Three-way handshake
    1.  This is how two different endpoints establish a connection.
        *   The three steps involved are:
            1.  SYN (Synchronize): The client sends a SYN packet to the server to initiate a connection.
            2.  SYN-ACK (Synchronize-Acknowledge): The server receives the SYN packet, acknowledges it, and sends back its own SYN packet to the client.
            3.  ACK (Acknowledge): The client receives the SYN-ACK packet, acknowledges it, and the connection is established.
    - However when you remove the headers for TCP and IP, it ends up being around 40 bytes total for all the headers
- Below is a representation of the packet as it travels up
- L3
  - [L3][L4][Data]
- L4
  - [L4][Data]
- L2 (Special case it has a trailer)
  - [L2][Payload][Trailer]
  - (Uses mac address)
- The whole process is called encapsulation and decapsulation
- L4
  - [L4][Data]
- L2 (Special case it has a trailer)
  - [L2][Payload][Trailer]

- The whole process is called encapsulation and decapsulation
  - Going down is encapsulation - encoding the data
  - Decapsulation is going up - stripping away the headers


### DNS
- Domain Name System is what we know [which translates human-readable domain names into machine-readable IP addresses], that's why we don't memorize IPs.
- ARP
  - Corresponding MAC address [which is a unique hardware identifier assigned to network interfaces]
- Port numbers are often known already (otherwise need to manually get)
  - 443 [(HTTPS, typically used for secure web browsing)]
  - 83 [(Commonly associated with Network Security Services (NSS) Daemon, but less frequently encountered in general web browsing)]
  - Web browser stuff [(This refers to ports commonly used by web browsers, such as 80 for HTTP and 443 for HTTPS)]
  - 83
  - Web broswer stuff
* bind(IpaddrB, portB)

* Problem Statement
  * Average brain can remember 7 digits for a few names [This is often referred to as Miller's Law or the Magical Number Seven, Plus or Minus Two.]
  * IP addresses have 12 digits [This refers to IPv4 addresses, which are 32-bit numbers often represented as four decimal numbers separated by dots, e.g., 192.168.1.1. This format typically results in around 12 digits.]
  * need easier way to remember IP addresses
* Solution:
  * Alphanumeric names to refer to hosts
  * Just as contacts or telephone directory (white pages) [Telephone directories list names alongside telephone numbers, analogous to how DNS lists hostnames alongside IP addresses.]
  * DNS to map between alphanumeric host names and binary IP addresses [DNS stands for Domain Name System.]
  * Address Resolution is the name for this [Address Resolution refers to the process of finding the network address (like an IP address) for a given host name.]
* Cannot have duplicate MAC addresses inside a network
  * 2^48 power MAC addresses exist [MAC addresses are 48-bit unique identifiers assigned to network interfaces.]
* 53 is DNS server port [The standard port for DNS queries is UDP port 53. TCP port 53 is also used for zone transfers.]
* Simple but does not scale
* Every new host needs to be entered in this table
* Performance Failure Questions
* Why not centralize DNS?
  * Single point of failure [If the central DNS server goes down, no one can resolve hostnames to IP addresses.]
  * traffic volume [A single server would have to handle all DNS requests, leading to congestion.]
  * distant centralized database [Accessing a faraway server can introduce latency.]
  * maintenance [Updating and managing a single, massive database is complex.]
  * In sum: doesn't scale

- DNS Root server
- Top-level domains (TLDs) are the highest level in the hierarchical Domain Name System (DNS) of the Internet. They appear at the end of a domain name.
  - .com (originally intended for commercial entities, now widely used by a variety of organizations)
  - .org (originally intended for non-profit organizations, now used more broadly)
  - .edu (restricted to degree-granting educational institutions)
- Country code domain name servers (ccTLDs) are two-letter TLDs that are associated with a particular country or territory.
  - .DE (Germany)
  - .UK (United Kingdom)
  - .AU (Australia)
  - .BE (Belgium)
  - .CH (Switzerland)

### Root DNS Servers
- 13 Root DNS Servers
  - a.root-servers.net,...m.root-servers.net
  - Logical (software) (The 13 names refer to logical servers, not necessarily distinct physical machines. These are often distributed across many actual servers.)
- A root server 198.41.94.177, 2001:503:ba3e::2:30
- C root server 192.33.4.12, 2001:500:2::c
- IP addresses are well-known and published
- Physically many more than 13 located around the world
- Load balancing and reliability

---
#### To connect to google server
1. www.google.com 
2. TCP connection - Three way handshake
   1. This is how two different endpoints estabish a connection
---
- Cyclic Redudancy Checkl
  - If data frame has error or not
  