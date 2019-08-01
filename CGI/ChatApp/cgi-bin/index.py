import json

file = open('chat_data.json')
chat = json.load(file)

file.close()

print("""
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">

    <title>Hello, world!</title>
    <style>
        ul {
            list-style:none;
            width:400px;
            height: 300px;
            overflow-y: scroll;
        }
        ul li {
            background-color : #eee;
            margin-bottom : 1px;
            padding: 10px;
        }
    </style>
  </head>
  <body>""")

print("""
<div class="container">
    <h2>Chat Room</h2>
    <hr>
    <div class="row">
        <div class="col-md-5">
            <form action="client.py" onsubmit="sendMsg()">
                  <div class="form-group">
                    <label for="msg">Enter Message</label>
                    <textarea name="msg" style='resize:none;' rows=10 class="form-control" id="msg" placeholder="Enter message"></textarea>
                  </div>
                  <button type="submit" class="btn btn-primary">Send</button>
            </form>
        </div>
        <div class="col-md-7">
            <label>ChatBox</label>
            <ul id="chat">
            </ul>
        </div>
    </div>
</div>
""")

print("""
    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
    
    <script>
        var ul = document.querySelector("#chat");
""")

for i in range(len(chat)):
    for key in chat[i]:
        print("""
        var li = document.createElement("li");
        li.innerHTML = "%s";
        var key = "%s";
        if (key == "msg"){
            li.style.textAlign = "right";
        }
        else {
            li.style.textAlign = "left";
        }
        ul.appendChild(li);
        """%(chat[i][key], key))

print("""
    </script>
  </body>
</html>
""")
