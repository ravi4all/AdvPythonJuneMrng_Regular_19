import cgi
import model
import base

form = cgi.FieldStorage()
email = form.getvalue("email")

data = model.profile(email)

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
        <link rel="stylesheet" href="styles.css">
    </head>

    <body>
    """)

base.header(email)

print("<div class='container'>")
print("""<h2>Edit Profile </h2>
<hr>
""")

print("""
<div class="row">
    <div class="col-md-4">
        <img src='../profile_pic/{}' class='w-100' alt="profile_pic">
    </div>
    <div class="col-md-8">
        <h3>Email : {}</h3>
        <h3>DOB : {}</h3>
        <h3>Interest : {}</h3>
        <h3>Occupation : {}</h3>
    </div>
</div>
""".format(data[0][-2], data[0][-1], data[0][1],data[0][3],data[0][2]))

print("</div>")
print("""
</body>
</html>
""")