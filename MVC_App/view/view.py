import sys
sys.path.append('..')
from controller import controller

def loginSuccess(data):
    while True:
        print("""
        1. Post
        2. View Profile
        3. Update Profile
        4. Delete Profile
        """)
        ch = input("Enter your choice : ")
        todo = {
            "1" : post,
            "2" : viewProfile,
            "3" : updateProfile,
            "4" : deleteProfile
        }
        email = data[0][1]
        todo.get(ch)(email)

def post(email):
    pass

def viewProfile(email):
    pass

def updateProfile(email):
    pass

def deleteProfile(email):
    pass

def login():
    email = input("Enter email : ")
    pwd = input("Enter pwd : ")
    data = controller.login(email,pwd)
    if isinstance(data, str):
        print(data)
        return
    else:
        loginSuccess(data)

def register():
    name = input("Enter your name : ")
    email = input("Enter your email : ")
    pwd = input("Enter your password : ")
    user = controller.register(name, email, pwd)
    print(user)

def main():
    print("""
    1. Login
    2. Register
    """)

    todo = {
        "1" : login,
        "2" : register
    }
    ch = input("Enter your choice : ")
    todo.get(ch)()

main()