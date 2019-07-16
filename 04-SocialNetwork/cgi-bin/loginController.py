import cgi
import model
import home

form = cgi.FieldStorage()
email = form.getvalue("login_email")
pwd = form.getvalue("login_pwd")

data = model.loginUser(email,pwd)
home.homePage(data)