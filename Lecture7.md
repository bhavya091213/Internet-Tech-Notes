Lecture7.md


# Lecture 7 - HTTP


### FORMAT
- Method SP URL SP version CR LF (carriage return line feed)
- header field name: value CR LF
- header lines
- header value
### Method types
- GET
  - Retrieves data from a specified resource.
- PUT
  - Updates a specified resource.
- POST
  - Submits data to be processed to a specified resource.
- DELETE
  - Deletes a specified resource.
- HEAD
  - Asks server to leave requested object out of response


### RESPONSE
- version [HTTP version] status code [numeric code] status phrase [textual description] cr lf (status line)
- header field name: value cr lf header lines
- cr lf
- entity body

### Status codes
- 200 ok
- 301 moved permanently (300)
- 404 not found
- 400 bad request (message not understood by server)
- 505 HTTP version not supported


### HTTP info
- Persistent vs Nonpersistent HTTP connections
  - What is the difference?
    - Nonpersistent HTTP: Each request/response pair is on a separate TCP connection. The connection is closed after the object is transferred. This can lead to higher latency due to the overhead of establishing new connections.
    - Persistent HTTP: Multiple request/response pairs can be sent over the same TCP connection. The connection is kept open for a period of time, reducing the overhead of connection establishment and improving performance.
- Cookies (User-server State)
  - Cookies are small pieces of data sent from a website and stored on the user's computer by the web browser while the user is browsing. They allow websites to remember information about the user, such as login credentials, items in a shopping cart, or user preferences. This allows for stateful interactions in an otherwise stateless protocol like HTTP.
- Web Caches
  - Web caches are intermediary storage systems that store copies of frequently requested web objects (e.g., HTML pages, images, scripts). When a user requests an object, the cache checks if it has a recent copy. If so, it serves the object directly, reducing latency and server load. If not, it fetches the object from the origin server, stores a copy, and then serves it to the user.
- Header Lines
  - Header lines are components of HTTP messages that provide metadata about the request or response.
  - If-modified-since
    - This is a conditional request header. The client sends this header to the server indicating that it only wants to retrieve the object if it has been modified since the date and time specified.
    - Example: `If-Modified-Since: Tue, 15 Nov 1994 12:45:26 GMT`
  - if-unmodified-since
    - This is also a conditional request header. The client sends this header to the server indicating that it only wants to perform the request (e.g., a PUT operation to update a resource) if the resource has not been modified since the specified date and time. If it has been modified, the server should respond with an error (e.g., 412 Precondition Failed).
    - Example: `If-Unmodified-Since: Tue, 15 Nov 1994 12:45:26 GMT`
  - cookie
    - This is a request header sent by the client to the server containing cookie data previously set by the server.
    - Example: `Cookie: sessionid=abcdef12345; username=johndoe`
  - set-cookie
    - This is a response header sent by the server to the client, instructing the client to store a cookie.
    - Example: `Set-Cookie: sessionid=abcdef12345; expires=Wed, 13-Jan-2021 12:00:00 GMT; path=/`


### Stateless vs stateful HTTP server
- Stateless
  - server maintains no information about past client requests [The server treats each request as an independent event, without any memory of previous interactions with the same client.]
- What state can bring:
  - Authorization (JWT) [JSON Web Tokens, used to securely transmit information between parties as a JSON object. They are often used for authentication and authorization.]
  - Shopping carts
  - recommendations
  - user session state
- Cookie keeping state:
  - Cooking file, usual http request msg, server creates ID 1678 for user Set-cookie 1678
  - Enteres in backend databse

### Head of Line Blocking
- HOL
- HTTP has concurrent requests; HTTP/1.1 has sequential requests.
  - (HTTP/1.1 handles requests one after another on a single connection, leading to a situation where a slow or blocked request can delay all subsequent requests.)
- With HTTP/1.1, one could have done independent TCP connections, allowing parallel processing.
  - Overhead is the problem.
    - (Establishing and maintaining multiple TCP connections incurs significant overhead in terms of network resources, processing power, and latency.)