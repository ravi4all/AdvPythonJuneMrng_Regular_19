import sys
sys.path.append('..')
from model import model

def login(email, pwd):
    data = model.login(email,pwd)
    return data

def register(name, email, pwd):
    user = model.register(name, email, pwd)
    return user