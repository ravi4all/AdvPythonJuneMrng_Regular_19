# Socket
# Sockets let app attach to the local network at different ports

# Basic Mechanism of Server Client App:
# 1.Client app sends request to server app
# 2.Server app returns a reply
# 3.Basic data communication b/w client and server:
# File Transfer : sends name and gets a file
# Web Page : sends url and gets a page
# Echo : sends a message and gets it back

# Server Socket
# 1. create a socket - Get the descriptor
# 2. bind to address - What port am I on?
# 3. listen on a port, and wait for a connection to be established
# 4. accept the connection from a client
# 5. send/recv the same way we read and write for a file
# 6. shutdown to end read/write
# close to release data

# Client Socket
# 1. create a socket
# 2. bind* - this is probably be unnecessary because you're client, not the server
# 3. connect to a server
# 4. send/recv - repeat until we have or receive data
# 5. shutdown to end read/write
# 6. close to releases data

