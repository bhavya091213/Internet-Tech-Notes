Lec-Notes-1.md


# Lecture 1 Notes - 09/2/2025


## What is a Network?
- Way to connect 2 or more entities with an Interconnection or link to carry some items
- Interconnection may happen over any medium
- Entities, link, carry
Example: Social Netowrks. Humans are the Entities, the Links are the conenctions, they Carry things like images, comments, etc


End goal is building systems and networks of scales. Understand design parameters and constraints.


## What is a Computer Network?
Carrier of information/bits between 2 or more computing entities
Interconnection or links can be any medium capable of communicating information:
- copper wire
- Lasers (optic fiber)
- microwave
- Cable (coax), satelite link
- Wireless link (cellular, 802.11, bluetoth)

## A single link network
- Send bits of data in packets or frames
- Need to worry about errors, how to convert bits into signals and vice versa
- Design parameters, what is the protocol, how many bits to send, etc

## Signle Link multiple access network (multi-access)
- Differentiate among many receivers
- Every host as a link layer address (MAC address)
- Packets or frames will have destination address
- Can't have every computer in the world on the same link   

## A network
- connect multiple links via routers
- Need to figure out how to route data packets from one host to another hosta

## Why networks?
- Availability of resources
  - Resources become available regardless of the user's physical location
- Load balancing
  - Jobs processed on least loaded machine
  - High Reliability
  - Alternative source of supply (multiple copies and redundancy)
- Human-to-Human Communication
  - e.., Messaging, Posts(blogs,images,videos), Telephone (Voice-over IP)
  
All this is possible due to networks, system design is important to manage these networks and build them reliably and with scalability in mind

## What is Internet Technology
- Network of networks
- A global internet based on the IP protocol
- Need to adopt a common language for the network to operate on
- The term "Internet Technology" refers to architectrue, protocols, and services (applicaitons)
- This course will focus on archictecure and protocols and specifications for message exchange between entities

## The Internet in a "nuts and bolts" view
- BIlliosn of connected computing devices
  - hosts are end systems
  - running netwroks apps at the Internet's edge
- Packet swithces forward packets and chunks of data either locally or to other networks
  - routers and switches are used
- Communication Links
  - things like fiber, copper, radio, and satellite.
  - transmission rate is measure and described through the use of the term "bandwidth"
- Networks
  - Collection of devices, routes, links: managed by an organization

## Internet Stakeholders
- ISPs - Internet Service Providers
  - Local ISPs - Tier 3 (cablevision)
  - Regional ISPs - Tier 2 (internap)
  - Global ISPs - (verizon, Sprint, ATT): they provide acccess to the entire internet by connecting ISP to otehr ISPs
- Peering ISPs
  - Have a mutual relationship about forwarding traffic of each others customers (no $ involved)
- Transit ISPs
  - Provides access to all reachable customers ($$ involved)
  - Global ISPs do this, charge based off consumption

## ISPs connected via Exchanges
- Internet Exchange Point, Flatter Internet
- BUsiness models among, content provider, transit providers, and customers
- Net Neutrality
- Allows for faster accesses
- IXP