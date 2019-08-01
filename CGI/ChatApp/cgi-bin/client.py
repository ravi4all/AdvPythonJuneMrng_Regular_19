import socket
import sys
import cgi
import json
import threading

form = cgi.FieldStorage()
msg = form.getvalue('msg')

file = open('chat_data.json')
chat = json.load(file)
file.close()

chat.append({"msg":msg})

file = open('chat_data.json','w')
json.dump(chat,file)
file.close()

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    
    <script>
        location.href = "http://localhost:9090/cgi-bin/index.py";
    </script>

  </head>
  <body>
  </body>
  </html>
""")

def main():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "127.0.0.1"
    port = 8989

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    soc.sendall(msg.encode("utf8"))
    data = soc.recv(1024)
    print(data)
    # file = open('chat_data.json')
    # chat = json.load(file)
    # file.close()
    #
    # chat.append({"rply": data.decode()})
    #
    # file = open('chat_data.json', 'w')
    # json.dump(chat, file)
    # file.close()

if __name__ == "__main__":
    threading.Thread(target=main).start()