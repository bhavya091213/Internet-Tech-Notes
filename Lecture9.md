Lecture 9.md

# Lecture 9 

### Recap
- browser cache
  - if modified since
- proxy cache
  - optimize multiple requests
- CDN



### Video
- ?v= [This appears to be a placeholder for a video identifier, common in URL parameters]
- Hash function that converts it [A hash function is a mathematical algorithm that maps data of arbitrary size to data of a fixed size. In this context, it likely converts the video ID into a format suitable for distribution or lookup.]
- Each video ID mapped to 192 names/urls
  - v[1-24].lscache.[1-8].c.youtube.com [These are example hostnames for Content Delivery Network (CDN) servers that serve video content.]
  - each host name returns IP address of CDN server [When a hostname is requested, the Domain Name System (DNS) resolves it to the IP address of a specific CDN server.]
  - CDN resolves each DNS request to multiple ID addresses [A CDN often has multiple IP addresses associated with a single hostname to ensure high availability and load balancing. This allows for faster delivery and reduces the impact of server failures.]
  - Copies are always made
### Netflix
- Stores copies of content (e.g., *Mad Men*) at its worldwide Open Connect CDN nodes.
- Subscriber requests content; the service provider returns a manifest.
- Peering networks (IXPs) [Internet Exchange Points].
  - Movie catalog connected to all service providers through ISPs.
### SMTP
- Simple Mail Transfer Protocol.
- Mail server and user agent.

### SMTP
- Simple mail transfer protocol
- mail server and user agent
* User agent
    * Talks to mail transfer agent
    * A mail transfer agent talks to another
    * Another user agent then reads the email
* Mail agents talk to other mail transfer agents through SMTP (Simple Mail Transfer Protocol)
    * SMTP has headers to know who you are sending to (domains -> DNS -> IP)
        * DNS (Domain Name System) is a hierarchical and decentralized naming system for computers, services, or other resources connected to the Internet or a private network. It translates domain names (like `example.com`) into numerical IP addresses (like `192.0.2.1`) that computers use to identify each other.
    * Port 25 is standard for email.
        * Port 25 is the default port for Simple Mail Transfer Protocol (SMTP), which is used for sending emails between mail servers. Other ports like 587 (for submission with authentication) and 465 (for SMTPS, an older, less secure method of encrypting SMTP) are also used.
- IMAP
- POP
- HTTP
- These are all access protocols
- How can browsers talk to port 25?
  - Web-based email
    - Requires a server that acts as an intermediary between the browser and port 25.
  - Request-response model
    - The browser sends a request, and the server sends a response.