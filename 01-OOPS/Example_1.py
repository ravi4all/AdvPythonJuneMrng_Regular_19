class User():
    users = []

    def __init__(self):
        pass

    def menu(self):
        print("""
        1. Login
        2. Register
        """)
        ch = input("Enter your choice : ")
        todo = {
            "1" : self.readUser,
            "2" : self.createUser
        }
        todo.get(ch)()

    def createUser(self):
        name = input("Enter your name : ")
        email = input("Enter your email : ")
        pwd = input("Enter your password : ")
        user = {"name":name, "email":email, "pwd":pwd}
        self.users.append(user)
        print(user)

    def readUser(self):
        pass

    def updateUser(self):
        pass

    def deleteUser(self):
        pass


obj = User()
obj.menu()