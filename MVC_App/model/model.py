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
    user = User(name, email, pwd)
    # users.append(user)
    query = "insert into users values (%s, %s, %s)"
    cursor.execute(query, (user.name, user.email, user.pwd))
    return user

def login():
    pass