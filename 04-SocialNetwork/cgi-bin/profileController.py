import cgi
import model
import base

form = cgi.FieldStorage()
mobile = form.getvalue("m_num")
dob = form.getvalue("dob")
occupation = form.getvalue("occupation")
interest = form.getvalue("interest")
# pic = form.getvalue("pic")
pic = form['pic']

model.editProfile(mobile,dob,occupation,interest,pic)

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

base.header()