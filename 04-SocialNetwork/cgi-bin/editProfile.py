import base
import cgi

form = cgi.FieldStorage()
email = form.getvalue("email")

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

<form action="profileController.py" method="post" enctype='multipart/form-data'>
<input type="hidden" value={} name="email">
  <div class="form-group">
    <label for="m_no">Enter Mobile No</label>
    <input type="text" class="form-control" id="m_no" name="m_num" placeholder="Enter Mobile No">
    <small id="emailHelp" class="form-text text-muted">We'll never share your mobile number with anyone else.</small>
  </div>
  <div class="form-group">
    <label for="pwd">Enter DOB</label>
     <input type="date" name="dob" class="form-control">
  </div>
  <div class="form-group">
    <label for="occ">Enter Occupation</label>
    <select name="occupation" id="occ" class="form-control">
        <option value="student">Student</option>
        <option value="employed">Employed</option>
        <option value="self-employed">Self Employed</option>
        <option value="engineer">Engineer</option>
        <option value="unemployed">Unemployed</option>
    </select>
  </div>
  <div class="form-group">
    <label for="interest">Select Interest</label>
    <select name="interest" id="interest" class="form-control">
        <option value="sports">Sports</option>
        <option value="education">Education</option>
        <option value="music">Music</option>
        <option value="travel">Travelling</option>
        <option value="gaming">Gaming</option>
    </select>
  </div>
  <div class="form-group">
  <label for="p_pic">Select Profile Pic</label>
    <input type="file" id="p_pic" name="pic">
  </div>
  <button type="submit" class="btn btn-primary">Submit</button>
</form>

""".format(email))

print("</div>")
print("""
</body>
</html>
""")