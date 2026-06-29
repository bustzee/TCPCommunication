# Python TCP Messaging System

A multithreaded client-server messaging application built from scratch using Python sockets. This project implements a custom messaging protocol using JSON packets and supports communication between multiple clients through a central server.

This project was created to explore:

- TCP socket programming
- Multithreading
- Client-server architecture
- Custom protocol design
- JSON serialization/deserialization
- Concurrent message handling


# Features
- Multiple clients can connect simulatenously
- Username based identification and messaging
- Client-client communication with server acting as the middle-man
- Custom JSON parsed messages
- Multithreaded server architecture

## Architecture
- The server acts as a central message router
- ```text
                 SERVER
                    |
        -------------------------
        |           |           |
      Alice        Bob       Charlie
        |           |           |
        +--------Messages-------+


  ```
- Each client:

  - Connects to the server
  - Registers a username
  - Sends JSON packets
  - Receives JSON packets asynchronously
 
- The server:
  - Maintains a dictionary of current clients connected
  - Receives and sends packets to individual clients
  - Routes messages to the intended recipient
  - Handles when a client disconnects
## Packet Structure
- All communication uses JSON packets
- ```json
  {
    "type": 0,
    "sender": "",
    "receiver": "",
    "content": "alice"
  }
  ```
  This type of message lets the server know what's the username of the client connecting to the server
- ```json
  {
    "type": 1,
    "sender": "alice",
    "receiver": "bob",
    "content": "Hello!"
  }
  ```
  This type of message lets the server know alice is trying to send a message to bob with the content of "Hello!"
- ```json
  {
    "type": 2,
    "sender": "alice",
    "receiver": "",
    "content": ""
  }
  ```
  Notifies the server that client is disconnecting

## Project Structure
```text
├── main.py
├── client_main.py
├── server.py
├── client.py
├── message.py
```
### File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Starts the server |
| `client_main.py` | Starts a client |
| `server.py` | Contains server logic and message routing |
| `client.py` | Contains client logic |
| `message.py` | Defines the message packet structure |

---

### Running a server
- To run a server simply run the main.py. It should output "LISTENING ON PORT 5000".

### Running a client
- To run a client simply run the client_main.py. It should ask you for your username. Note that in order to run the client_main.py the server should already be running.
