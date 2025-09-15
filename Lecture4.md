Lecture4.md
# Lecture 4 - Switching
### Comparisons
- Header overhead
  - Circuit < message < packet
- Transmission Delay
  - Short bursty messages:
    - Packet < message < circuit
  - Long Continuous Messages:
    - Circuit < message < packet
Having a packet size be very large would reduce overhead, however if you lose a packet you lose a lot of data.
If you shrink the packets, there is more overhead, however you can get more pipelining.
This is a tradeoff that is important for understanding what happens at your link layer.
- Probability of loss
  - Affects system design
### Packet vs Circuit Switching
- Example:
  - 1 Gb/s link, each user 100 Mb/s when active, active 10 percent of the time
  - Under circuit switching we can have 10 users.
  - With packet switching we can have 35 users since the probability of more than 10 users being active at the same time is less than 0.0004.
  - How do you get the 0.0004?
    - This probability can be calculated using the binomial distribution, where $n$ is the number of users, $k$ is the number of active users, and $p$ is the probability of a single user being active.
    - The formula for the binomial probability is:
        $$ P(X=k) = \binom{n}{k} p^k (1-p)^{n-k} $$
    - In this scenario, we are interested in the probability that more than 10 users are active. This can be calculated by summing the probabilities for $k=11, 12, \ldots, 35$.
        $$ P(X > 10) = \sum_{k=11}^{35} \binom{35}{k} (0.1)^k (1-0.1)^{35-k} $$
    - The question likely refers to a specific calculation for the probability that at least 11 users are active simultaneously out of 35 users, given each user has a 10% chance of being active. The calculation would involve summing probabilities from $k=11$ to $k=35$ using the binomial probability formula.
  - Effects system design


### Measuring Network Performance

*   **Packet length**: size of a packet (units are bits or bytes)
*   **Channel speed or bandwidth**: how fast the channel can transmit bits (units = bits/second, bytes/second, or packets/second)
*   **Packet transmission time**: amount of time to transmit an entire packet (units = seconds)
    *   This can be calculated using the formula:
        $$ \text{Packet Transmission Time} = \frac{\text{Packet Length}}{\text{Channel Speed}} $$
*   **Propagation delay**: Delay imposed by the properties of the link. Depends on the link's distance (units = seconds)
*   **Total transfer time** = propagation delay + packet transmission time
    *   This can be expressed as:
        $$ \text{Total Transfer Time} = \text{Propagation Delay} + \frac{\text{Packet Length}}{\text{Channel Speed}} $$


Example:
- Packet length = 1500 bytes
- Channel capacity = 10 Mbps
- Propagation delay factor = 5 microseconds/km
1. How long does it take a single bit to travel on the link from A to B?
   * transmission + propagation
   * Channel speed is 10,000,000 bits per second
   * Propagation is 5 microseconds /km (Assuming a link length, for example, 500 meters is 0.5 km, the propagation delay would be 5 microseconds/km * 0.5 km = 2.5 microseconds)
   * Answer is: [The time for a single bit to travel the link is determined by the propagation delay, not the transmission time, as it's about a single bit moving across the physical medium.]
2. How long does it take A to transmit an entire packet onto the link?
   1. Length = 1500 bytes
   2. Speed is 10 Mbps
   3. 1.2 msec is the answer (provide the work)
      * To calculate the transmission time, we use the formula:
        $$ \text{Transmission Time} = \frac{\text{Packet Size}}{\text{Channel Capacity}} $$
      * First, convert packet size to bits: 1500 bytes * 8 bits/byte = 12000 bits
      * Convert channel capacity to bits per second: 10 Mbps = 10,000,000 bits/second
      * $$ \text{Transmission Time} = \frac{12000 \text{ bits}}{10,000,000 \text{ bits/second}} = 0.0012 \text{ seconds} $$
      * Convert seconds to milliseconds: 0.0012 seconds * 1000 milliseconds/second = 1.2 milliseconds


### Packet delay: four sources

1.  transmission [This refers to the time it takes to send all the bits of a packet from one router to the next.]
2.  Nodal Processing [This is the time a router spends examining packet headers, determining where to send the packet, and checking for errors.]
3.  Queuing [This is the time a packet waits in a queue (buffer) before being transmitted onto the outgoing link. It depends on the router's congestion level.]
4.  Propagation [This is the time it takes for a bit to travel from the sender to the receiver across the physical link. It depends on the physical medium (e.g., cable, fiber optic).]
$d_{nodal} = d_{proc} + d_{queue} + d_{trans} + d_{prop}$
Where:
*   $d_{nodal}$ is the total delay at a node.
*   $d_{proc}$ is the nodal processing delay.
*   $d_{queue}$ is the queuing delay.
*   $d_{trans}$ is the transmission delay.
*   $d_{prop}$ is the propagation delay.


### Message switching vs Packet Switching
Link speed is 1000 Bytes/s (ignore propagation delay), packet size is 100 Bytes, file size is 1000 Bytes
Find total time to transfer the entire file under the two switching techniques

- Message switching
    - If I want to send 1000 bytes on a 1000 Bytes/s link, it would take 1 second to transmit the entire message from Computer 1 to R1, and another 1 second to transmit from R1 to Computer 2, totaling 2 seconds.
        - Transmission time for one hop = File Size / Link Speed = 1000 Bytes / 1000 Bytes/s = 1 second
        - Total transmission time = Transmission time to R1 + Transmission time to Computer 2 = 1 second + 1 second = 2 seconds
- Packet switching
    - A packet would take 0.1 seconds to transmit [100 Bytes / 1000 Bytes/s].
    - The file is chopped into 10 packets [1000 Bytes / 100 Bytes/packet].
    - Pipelining reduces the overall time.
    - Total time for packet switching can be approximated as:
        - (Number of packets * Transmission time per packet) + (Number of hops * Processing delay per hop * Number of packets)
        - For this simplified example, ignoring processing delay for the sake of direct comparison with the message switching calculation:
            - Transmission time for the first packet to R1 = 0.1 seconds
            - Transmission time from R1 to Computer 2 = 0.1 seconds
            - Since all packets are sent sequentially and R1 processes them, there's an overlap. The total time is the time to transmit the first packet, plus the time for all subsequent packets to transmit and traverse the second link.
            - Total time (simplified) = Transmission time of first packet + (Number of packets - 1) * Transmission time of subsequent packets + Transmission time for last packet across second link
            - A more common simplified model for total transfer time with pipelining and no processing delay:
                - (Number of packets * Transmission time per packet) + (Transmission time for the last packet to traverse all links)
                - However, given the example's 1.1 seconds, it implies some form of sequential processing per hop.
            - Let's use the provided 1.1 seconds as a result of pipelining and minimal delays.
            - [Note: The provided 1.1 seconds is a simplification. A more detailed calculation considering the pipeline effect would be:
                - Time to send first packet to R1: 0.1s
                - Time for R1 to process first packet (assumed negligible here for this comparison)
                - Time for R1 to send first packet to Computer 2: 0.1s
                - This means the first packet arrives at Computer 2 at 0.2s.
                - However, the entire file transmission is complete when the *last* packet arrives at Computer 2.
                - With pipelining, as soon as the first packet starts transmitting from R1, the second packet can start transmitting from Computer 1 to R1.
                - Total time = Transmission time of first packet to R1 + (Number of packets - 1) * Transmission time per packet + Transmission time of last packet from R1 to Computer 2
                - Total time = 0.1s + (10 - 1) * 0.1s + 0.1s = 0.1s + 0.9s + 0.1s = 1.1s. This calculation matches the provided 1.1 seconds.]
    - Processing delay hurts packet switching the most since each packet gets that delay added [per hop].
Packet would take 1.1 seconds, everything is chopped into 10 so pipelining reduces time

Procesing delay hurts packet switching the most since each packet gets that delay added


Circuit switching has reservation built into it. Packet switching doesn't have that concept, allowing queuing to form

Circuit switching however is subject to packet switching


### Application Layer
* Request response
* Format:
  * Synrax -> What fields in messages and how fields are delineated
  * Smeantics: meaning of information in fields
* Rules for when and how processes send and respond to messages
* Public domain protocols
  * Defined in RFCs (Request for Comments - a series of documents that describe many Internet standards and protocols)
  * Allows for interoperability
  * HTTP (Hypertext Transfer Protocol), SMTP (Simple Mail Transfer Protocol)
  * Proprietary protocols as well like KaZaA, RealAudio
- Non-network applications are applications that execute on a single host.
- Consider two applications on two different hosts connected by a network.
- In order to communicate, need to identify the parties.
- Computers have IPv4 and IPv6 which are their IP addresses (IPv4 addresses are 32 bits, and IPv6 addresses are 128 bits respectively).
- HEX is IPv6. [This is a common shorthand for hexadecimal notation, which is used to represent IPv6 addresses.]
- So need IP + port in order to communicate.
- Computers had IPv4 and IPv6 which are their IP addresses (IPv4 addresses are 32 bits, and IPv6 addresses are 128 bits respectively).