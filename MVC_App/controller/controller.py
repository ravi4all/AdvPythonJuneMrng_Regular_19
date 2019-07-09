import sys
sys.path.append('..')
from model import model

def login():
    pass

def register(name, email, pwd):
    user = model.register(name, email, pwd)
    return user