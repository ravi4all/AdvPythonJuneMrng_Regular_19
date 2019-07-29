# Server

import socket

# Create socket object
s = socket.socket()
print("Socket successfully created")


# Reserve a port on your computer
port = 9999

# Now bind to port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
s.bind(('localhost',port))
print("Socket binded to %s"%(port))

# Put the socket into listening mode
s.listen(5)
# we put the server into listen mode.5 here means that 5
# connections are kept waiting if the server is busy and
# if a 6th socket try to connect then the connection
# is refused.
print("Socket is listening")

message = "Thankyou for connecting"

while True:
    # Accept connection from client
    c,addr = s.accept()
    print("Got connection from",addr)

    # Send a thankyou message to the client
    c.send(message.encode('utf-8'))

    # Close the connection
    c.close()