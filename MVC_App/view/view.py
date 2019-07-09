import sys
sys.path.append('..')
from controller import controller

def login():
    pass

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