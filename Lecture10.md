# Lecture 10 - Application vs Transport
- Application layer: end-user communication of content (email, webpages).
- Transport layer: logical communication between processes.
  - Relies on enhanced network layer services.
- End-to-end (E2E) demultiplexing.
- A WebSocket always has an IP address and port number.
  - The port is used to demultiplex [traffic to the correct application process].
  - The IP address is the host [identifying the specific computer or device on the network].
- Just using an IP address can deliver a packet to the host. Using the port number at the transport layer, we can demultiplex [the traffic] to go to the right application.
- That's the reason why, at the receiving end, port numbers have to be unique [to ensure that incoming data is routed to the correct application process running on the host].
  - port is used to demultiplex
  - Address is the host
- Just using address can deliver packet to the host and using port at transport layer we can demultiplex to go to the right application
- Thats the reason why at the receiving end port numbers have to be unique

Transport is the logical communication between processes, network layer logical communication between hosts
- Transport network is HTTP TCP IP to network then up to HOST SOCKET APP


### Layering/demultiplexing
- Sending data
  - port S [Source Port]
  - IP S [Source IP Address]
- Receive data
  - port R [Destination Port]
  - IP [Destination IP Address]
- The payload looks like this
- Link Layer Mac S [Source MAC Address] Mac D [Destination MAC Address] ipv4 [IPv4 Protocol] or ipv6 [IPv6 Protocol]
  - then another header IP_S [Source IP Address] IP_D [Destination IP Address] IP ADDR [IP Address] and either thru udp [User Datagram Protocol] or tcp [Transmission Control Protocol]
  - then port S [Source Port] and port R [Destination Port]
  - then payload
- The header at the link layer will let you know [if the packet uses] IPv4 and IPv6.
- All issues need to [be] solved [as] end-to-end (E2E) issues, and that's what the transport layer handles.
- What can go wrong?
  - Packets can be corrupted.
    - Read and write of bits can cause bit flips.
    - [This is detected using a] CHECKSUM.
  - Packets can be lost at the host or somewhere in the network.
  - Packets can be duplicated.
  - Packets can take different paths and come out of order.
  - Or they can be delayed as their paths can be subject to delays.
  - 