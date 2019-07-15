import cgi
import model
import home

form = cgi.FieldStorage()

name = form.getvalue('reg_name')
email = form.getvalue('reg_email')
pwd = form.getvalue('reg_pwd')
city = form.getvalue('reg_city')
gender = form.getvalue('gender')

user = model.register(name, email, pwd, city, gender)

home.homePage()