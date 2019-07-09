class User():
    def __init__(self, name, email, pwd):
        self.name = name
        self.email = email
        self.pwd = pwd

    # tostring
    def __str__(self):
        return self.name + "," + self.email + "," + self.pwd

user = User('Ram','ram@gmail.com','1234')
print(user)