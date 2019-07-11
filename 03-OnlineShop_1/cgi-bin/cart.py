import base
import cgi
import json

file = open('data.json')
products = json.load(file)

form = cgi.FieldStorage()
p_id = form.getvalue('p_id')

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <style>
        body {
            background-image : url("http://cdn.osxdaily.com/wp-content/uploads/2011/10/NSTexturedFullScreenBackgroundColor.png");
        }
        h1 {
            color : #fff;
        }
    </style>
</head>
<body>
""")

base.header()

print("""
<div class="container">
    <h1 class="text-center">My CART</h1>
    <hr>
    <div class="row">
""")



print("""
</div>
</div>
""")

base.footer()