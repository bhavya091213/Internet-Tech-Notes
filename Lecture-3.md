Lecture-3.md


# Lecture 3 - TCP/IP Layering Structure
### Recap of Four Layers
1.  Application
    1.  Runs on ports of a network so we know [the] address
2.  Transport
    1.  Reliable byte-oriented stream
3.  Network
    1.  Hosts drop packets into this layer, this layer routes towards [the] destination -> **best effort** (only promise)
4.  Host to Network

### Application Layer:
Application layer protocols are application-dependent, varying per what the actual app is.

The Application layer provides session support and presentation support.
- Session support manages the dialogue between applications, ensuring that communication is orderly and that data is sent and received correctly. [This involves establishing, maintaining, and terminating connections.]
* Presentation support ensures that data is formatted in a way that the receiving application can understand. [This can include data encryption, compression, and translation.]
* session state:
* encryption:
* encoding:
On application layer, stuff like encryption, authentication, etcetera, happens all on the application layer.
Hides the details of the network from the session layer.
* IF we wanted to replace a point-to-point link with a satellite link, this change should not affect the behavior of the upper layers.
This is how it provides reliable end-to-end communication.
There are two main protocols.

### Transport Layer

Hides the details of the network from the session layer
- IF we wanted to replace a point-to-point link with a satellite link, this change should not affect the behaviour of the upper layers

This is how it provides reliable end to end communication

There are two main protocls
- TCP
  - Transmission control protocol
  - reliable
- UDP
  - User Datagram Protocol (UDP)
    - A connectionless transport layer protocol that prioritizes speed and simplicity over reliability. It does not guarantee delivery, ordering, or error checking.

### Network Layer
    - [This is a mechanism to prevent overwhelming the receiver. The transport layer (e.g., TCP) uses acknowledgments (ACKs) to confirm receipt of data. If the receiver is struggling to process the data, it will not send ACKs, effectively slowing down the sender.]
  - Method of **flow control**:
    - [This section would typically detail specific flow control mechanisms like sliding windows or stop-and-wait protocols.]
- **Congestion Control:**
  - The receiver might be capable of what it's receiving, however, the network may be throttled.
    - [Congestion control addresses the overall network capacity, whereas flow control deals with the capacity of the end-to-end connection between two hosts. A network can become congested due to multiple hosts sending data simultaneously, exceeding the capacity of intermediate routers or links.]
    - Some methods to solve are to restrict traffic:
        - Slowly reduce output of packets.
        - Dynamically adjusting at the rate you send is **congestion control** [managing the amount of data sent over a network to prevent overload].


Both flow control [managing the rate of data transmission between two endpoints] and congestion control are integral for the transport layer.

In sum:
- Performs end to end flow control
  - Any sort of end to end functionality
- Performs packet retransmission when packets are lost by the network 

### Network Layer

Helps define where the host is located. Answers questions like which host or which name?
Mainly responsible for routing decisions
- Dynamic routing
- Fixed routing
### Host to Network Layer
Main functionality is the transmission of a raw bit stream. It forms the physical interface between devices
There are some issues:
- Which modulation technique? (encoding bits into electrical or optical signals, e.g., Non-Return-to-Zero (NRZ), Manchester encoding)
- How long will a bit last? (This refers to the bit duration or bit period, which is the inverse of the bit rate: $T_b = 1/R_b$, where $T_b$ is the bit period and $R_b$ is the bit rate)
- Bit-serial or parallel transmission?
  - USB is serial (data is transmitted one bit at a time)
  - Lots of parallel bits cables get huge (transmitting multiple bits simultaneously requires multiple wires, leading to thicker and more complex cables)
- Simplex
    - One way (if you want to receive, you need to send through another interface)
  - Duplex
    - Both ways (simultaneous transmission and reception)
  - Half-Duplex
    - Something like a walkie-talkie
    - Can transmit and receive, but not simultaneously
- How many pins does the network connector have?
    * (This question is asking about the physical connector used for networking, such as an Ethernet RJ45 connector.)
- How is a connection set up or torn down?
    * (This question pertains to the protocols and processes involved in establishing and terminating network communication sessions.)

- NIC
  - Network Interface card

#### Data link layer
- Provides reliable transfer of information between two adjacent nodes
- Creates frames, or packets, from bits and vice versa
- Provides frame-level error control
- Provides flow control
In summary, the data **link** layer **provides** the network layer with what appears to be an error-free link for packets

Even though there is link-to-link reliability, transport layer still needs another guarantee of reliability since anything can go wrong at any step therefore just because the link layer is reliable doesnt guarantee reliability elsewhere

### Terminology
- Network: Collection of interconnected machines
- Host: Machine running user Application
- Subnet: Subset of the network, responsible for carrying messages between hosts
- Channel: Logical line of communication
- Topology: Network configuration
- Router: Process packets and routes packets towards the destination
- Protocol: Rules of communication


### Physical Transmission

*   **Binary Signal:**
    (A binary signal, in its simplest form, alternates between two distinct voltage levels, typically representing 0s and 1s. This can be visualized as a square wave.)
    - The problem is you would need some sort of clock rate in order to know how many adjacent 1 or 0 signals
    - Typical to use a triggered wave
      - Can count number of transitions instead of how long
*   **Amplitude Modulation (AM):**
    (In Amplitude Modulation, the amplitude (strength or height) of a carrier wave is varied in proportion to the information being transmitted. The frequency and phase of the carrier wave remain constant.)
    *   [Visual representation of AM:]
        (Imagine a steady, high-frequency wave (the carrier wave). The peaks and troughs of this wave are made taller or shorter according to the signal you want to send. If the signal is high, the carrier wave's amplitude increases; if the signal is low, the carrier wave's amplitude decreases.)
*   **Frequency Modulation (FM):**
    (In Frequency Modulation, the frequency of a carrier wave is varied in proportion to the information being transmitted. The amplitude and phase of the carrier wave remain constant.)
    *   [Visual representation of FM:]
        (Here, the carrier wave's frequency (how often its cycles repeat) is changed. When the information signal is high, the carrier wave's frequency increases (cycles are closer together). When the information signal is low, the carrier wave's frequency decreases (cycles are farther apart). The height of the carrier wave stays the same.)
*   **Phase Modulation (PM):**
    (In Phase Modulation, the phase of a carrier wave is varied in proportion to the information being transmitted. The amplitude and frequency of the carrier wave remain constant.)
    *   [Visual representation of PM:]
        (In Phase Modulation, the timing of the carrier wave's cycles is shifted. When the information signal is high, the phase of the carrier wave is advanced (shifted forward). When the information signal is low, the phase is retarded (shifted backward). The height and rate of the carrier wave's cycles stay the same, but their position in time changes.)


### Switching Schemes

1. Circuit Switching
2. Message Switching (Store-and-Forward)
3. Packet Switching (Store-and-Forward)