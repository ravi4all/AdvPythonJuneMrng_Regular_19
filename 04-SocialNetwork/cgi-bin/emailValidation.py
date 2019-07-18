import cgi
import model
import json, sys

def output(content):
    print("Recieved AJAX Call...")
    sys.stdout.write('Content-Type: text/plain\n\n')
    sys.stdout.write(content)

form = cgi.FieldStorage()

email = form.getvalue("email")
msg = model.emailValidation(email)
output(msg)
