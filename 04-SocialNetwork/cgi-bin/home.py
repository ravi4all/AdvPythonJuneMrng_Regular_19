import base

def homePage(data):
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

    base.header(data[0][1])

    print("<div class='container'>")

    print("<h3>Welcome {}</h3>".format(data[0][0]))
    print("</div>")
    print("""
    </body>
    </html>
    """)