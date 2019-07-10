import cgi

form = cgi.FieldStorage()

name = form.getvalue('name')
email = form.getvalue('email')
pwd = form.getvalue('pwd')

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<h1>Register Successfull</h1>
<h2>Name : {}</h2>
<h2>Email : {}</h2>

</body>
</html>
""".format(name, email))