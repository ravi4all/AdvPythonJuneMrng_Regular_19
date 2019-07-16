import pymysql
import os
connection = pymysql.connect(host='localhost',port=3306,user='root',
                             database='socialNetwork',autocommit=True)

cursor = connection.cursor()

class User():
    def __init__(self, name, email, pwd, city, gender):
        self.name = name
        self.email = email
        self.pwd = pwd
        self.city = city
        self.gender = gender

    def __str__(self):
        return self.name + "," + self.email + "," + self.pwd + "," + self.city + "," + self.gender

# users = []

def register(name, email, pwd, city, gender):
    try:
        user = User(name, email, pwd, city, gender)
        # users.append(user)
        query = "insert into users values (%s, %s, %s, %s, %s)"
        cursor.execute(query, (user.name, user.email, user.pwd, user.city, user.gender))
        return user
    except pymysql.IntegrityError:
        return "Email ID Already Exist"

def loginUser(email,pwd):
    query = "select * from users where email=%s and pwd = %s"
    cursor.execute(query, (email, pwd))
    # data_length = cursor.rowcount
    data = cursor.fetchall()
    if len(data) < 1:
        return "User do not exist"
    else:
        return data

def editProfile(mobile,dob,occupation,interest,pic):
    if pic.filename:
        # print("Image is",image)
        # print("Filename is",image.filename)
        fn = os.path.basename(pic.filename)
        open("profile_pic/" + fn, 'wb').write(pic.file.read())
        print("Image Saved Successfully...")