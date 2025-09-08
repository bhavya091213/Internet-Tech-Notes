Lecture-2-notes.md


# Lecture 2 - Layers and Internet Applications

## - Lecture 1 Recap
- ISPs are part of the transit layer (called transit entities)
  - They are connected via exchanges (IXP) which help provide a flatter internet. (IXPs, or Internet Exchange Points, allow different networks to connect and exchange traffic locally, reducing latency and cost.)
  - Net Neutrality (Net Neutrality refers to the principle that Internet service providers should treat all data on the Internet equally, not discriminating or charging differently by user, content, website, platform, application, type of attached equipment, or method of communication.)
  - ISPs are also providers (ISPs provide internet access to end-users.)
  - From local to regional to global and then it goes the same path down to your destination. (Traffic often follows a hierarchical path: from a local ISP, to a regional ISP, then a global (Tier 1) provider, and then reverses the path to reach the destination network and the intended recipient.)
  - Global ISPs are peers
- IXP (Internet Exchange Point)
  - Pairwise connectivity to peers. *[Note: IXPs facilitate direct interconnection between networks, allowing them to exchange traffic without traversing the public internet.]*
  - Lets say we have three peers, A, B and C, and B and A are peered. However, we need to transfer from A to C, we can either re-pair or we can transit. *[Note: "Re-pair" means establishing a direct peering relationship between A and C. "Transit" means relying on another network (e.g., B) to carry traffic from A to C.]*
  - So in sum, IXPs are pairwise and symmetric, not transitive like ISPs. *[Note: Symmetric peering means that both networks send and receive roughly equal amounts of traffic from each other. ISPs provide transitive connectivity, meaning traffic can reach any destination on the internet.]*
  - Fundamental architecture of today. *[Note: IXPs are a critical part of the modern internet infrastructure, reducing latency and improving network performance.]*
  - Netflix switched from ISPs to having IXPs. They had multiple peering points and the cable provider is connected to Netflix (Netflix directly delivers to cable provider). *[Note: This is a Content Delivery Network (CDN) strategy. By directly interconnecting with ISPs via IXPs, Netflix can improve the quality of video streaming for its users.]*
- For ISP, its $/infinite usage, IXP its $/consumption. *[Note: ISPs typically charge end-users a fixed monthly fee for internet access, regardless of usage. IXPs typically charge their members based on the amount of traffic they exchange.]*
- Difference between IXP and ISP. *[Note: ISPs provide internet access to end-users. IXPs provide interconnection services between networks (ASNs).]*



## Internet Applications

The web used to be read only, transitioned to read write (POST) you could post things and write to the internet. Personalization / location dependent was the next step
Now we are in the age of generative web and AI

### Types of Networks in an Internet

- Local Area Networks
  - Managed within one administrative domain (typically)
  - Privately owned, within building
  - High speed, broadcast, ethernet, wifi, bluetooth
  - 2 to 100 Mbps to 10s of Gbps
  - Example: Rutgers (despite large campus its all managed under one domain)
- Wide Area Networks
  - Spans a large area
  - Point-to-point, high speed fiber or trunk lines
    - Long delays but very high speed links
    - Several Gbps
  - City to City or Country to Country (Long Haul Networks)
    - Note: These networks typically utilize technologies like Synchronous Optical Networking (SONET) or Synchronous Digital Hierarchy (SDH) for reliable, high-bandwidth communication over long distances.
- Mostly optic fiber is used for long haul networks [Note: "Optic fiber" is commonly referred to as "optical fiber."]
Networking is also often measured in bits compared to file transfers [Note: Networking speed and bandwidth are typically measured in bits per second (bps), while file sizes are typically measured in bytes. 8 bits = 1 byte.]
Wireless networks are hosted by infrared or radio links
- Local area and wide area [Note: Local Area Networks (LANs) connect devices within a limited area, such as a home, school, or office. Wide Area Networks (WANs) connect devices over a larger geographical area.]
- Also have satellite networks [Note: Satellite networks use satellites to provide internet access or network connectivity, especially in remote areas.]
- Cellular networks are also considered wide area [Note: Cellular networks use cell towers to provide wireless communication services over a wide geographical area, making them a type of WAN.]
- Also have satellite netwroks
- Cellular networks are also considered wide area


### Protocols
Protocols are the building blocks of a network architecture
Each protocol object has two different interfaces
- Server interface
  - Operations on this protocol (e.g., configuration, monitoring)
- Peer to peer interface
  - Messages exchanged with peer (e.g., data transfer, control signals)
The term protocol refers to both the specification (the documented standard) and the implementation of the module. (the actual code that executes the protocol).
  - Messages exchanged with peer

The term protocol refers to both the specification and the implementation of the module

### Internet Architecture
- Defined by Internet Engineering Task Force (IETF)
- Hourglass Design
  - Anything over IP, IP over anything
  - The architecture can be described in two ways, all of the protocols that run above IP in the layers and IP can run over any type of link
  - This is a fundamental characteristic of the modern internet architecture
The internet used to be based off 7 layers, the current architecture is 4 layers of protocols.

#### LAYER 1: APP LAYER [Application Layer]
- This is the application layer
- Some protocols:
  - HTTPS
  - HTTP
  - FTP (File Transfer Protocol)
  - SIP
  - QUIC
  - Sometimes SIP can be TCP as well
- Every application will run on a different port
- Cannot have duplicate portes, unique ports
#### LAYER 2: TRANSPORT LAYER
- TCP and UDP are the most prominent [Transmission Control Protocol and User Datagram Protocol respectively]
- Takes care of transporting the message into the proper format, bitstream, etc. 
  - (Bitstream is a contiguous sequence of bits, representing data)
  - Uses the port number as an identifier.
#### LAYER 3: NETWORK LAYER
- Labeled the IP layer (network layer).
- Just sends packet to the receiver
- Only responsible with best effort possible to send message
- IP can be IPv4 and IPv6
#### LAYER 4: HOST TO NETWORK LAYER
- Takes care of transporting the message into the proper format bitstream etc 
- This happens so the end host can take that message
  - (Bitstream: A contiguous sequence of bits, representing data.)
- Takes care of transporting the message into the proper format bitstream etc
- This happens so the end host can take that message


### Why layering?
Network communication is very complex [complexity] with lots of diversity and range. As a consequence, [it] needs simplification through abstraction in layers
Testing and maintenance is simplified when you have layering. It is easy to replace a single layer with a different version
  - Layering Benefits:
    * Simplifies complexity
    * Eases testing and maintenance

