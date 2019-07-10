import pymysql
connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='db_demo_2',autocommit=True)

cursor = connection.cursor()

class User():
    def __init__(self, name, email, pwd):
        self.name = name
        self.email = email
        self.pwd = pwd

    def __str__(self):
        return self.name + "," + self.email + "," + self.pwd

# users = []

def register(name, email, pwd):
    try:
        user = User(name, email, pwd)
        # users.append(user)
        query = "insert into users values (%s, %s, %s)"
        cursor.execute(query, (user.name, user.email, user.pwd))
        return user
    except pymysql.IntegrityError:
        return "Email ID Already Exist"

def login(email,pwd):
    query = "select * from users where email=%s and pwd = %s"
    cursor.execute(query, (email, pwd))
    # data_length = cursor.rowcount
    data = cursor.fetchall()
    if len(data) < 1:
        return "User donot exist"
    else:
        return data
