Lecture6.md

# Lecture 6 - DNS protocol and messages
### Protocol
QR OPCODE
- Also has a 16 bit header
- Within 12 bytes
  - Identification | Flags
  - Number of questions | Number of answer RRs
  - Number of authority RRs | Number of additional RRs
- Then The rest is questions and resource records
- Let's say we look for www.tiktok.com
  - That is a question
  - The root server answers what it can and then gives an answer
  - Iteratively goes through the rest
- Let's say we want ilab.cs.rutgers.edu
  - a.edu server finds rutgers.edu and then it goes to cs then goes to ilab.
  - Then the answer gets filled eventually
**NOTE**
- Root server is always iterative
  - What does this mean and how does it compare?
    - Iterative query: The DNS resolver (client) makes a request to a DNS server, and the server responds with the best information it has. If it doesn't have the complete answer, it provides a referral to another DNS server that might have the answer. The client then queries the referred server, repeating this process until it gets the final answer or an authoritative response. This contrasts with a recursive query, where the DNS server is expected to provide the full answer to the client, handling all the necessary lookups itself.
- Root server will not know IP, it will know .com server (nameservers)



### DNS Query
- Different record types
  - MX (Mail Exchanger: directs mail to specific mail servers)
  - CNAME (Canonical Name: creates an alias for one domain name to another)
  - NS (Name Server: specifies the authoritative name servers for a domain)
- Iterative vs. Recursive servers
  - Iterative queries: The DNS resolver returns a referral to the next server to query.
  - Recursive queries: The DNS resolver tries to get the final answer from the DNS servers.

### Web and HTTP
- Web page consists of objects
- Object can be HTML file, JPEG image, Java applet, audio file
- A web page consists of a base HTML file which includes several referenced objects
- Each object is addressable by a URL
- www.cs.rutgers.edu/undergraduate/pic.gif
  - [This URL can be] split between host name and path name
    - Host name: www.cs.rutgers.edu
    - Path name: /undergraduate/pic.gif

### HTTP MESSAGES
- ASCII Human-readable format
- GET, POST, HEAD commands
  - Method, path, HTTP/1.1
    - This describes the first line of an HTTP request, also known as the request line. It typically includes the HTTP method (e.g., GET, POST), the path of the requested resource, and the HTTP protocol version.