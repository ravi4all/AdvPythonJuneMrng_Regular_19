import socket
import sys

# ip = socket.gethostbyname('www.brain-mentors.com')
# print(ip)

# Stream - Flow of data
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket successfully created")

except socket.error as err:
    print("Error :",err)

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname('www.google.com')

except socket.gaierror:
    print("Error occurred")
    sys.exit()

# Connecting to server
s.connect((host_ip, port))

print("Successfully connected to google on port",host_ip)