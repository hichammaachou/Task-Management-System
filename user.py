import json
from typing import Any
class AuthenticatedUser:
    _instance = None
    _authenticated_user = None
    def __new__(cls):
        if cls._instance == None:
            cls._instance = super().__new__(cls)
            return cls._instance
    def authenticated_user(self):
        return self._authenticated_user 
    def authenticated_user(self, user):
        self._authenticated_user = user   
    def sign_out(self):
        self._authenticated_user = None


class User:
    def __init__(self, username, password,email):
        self.username = username
        self.password = password
        self.email = email

AuthenticatedUser1 = AuthenticatedUser()
user_data = []
try:
    with open('users.json', 'r') as file:
        user_data = json.load(file)
except FileNotFoundError:
    print('File not found!')
    quit()      


def sign_up():
    while True:
        
        username = input('Enter a username: ')
        for i in range(len(user_data)):
            while username == user_data[i]["username"]:
                print('Username already in use!')
                username = input('Enter a username: ')
        break

    email = input('Enter your email: ')
    password = input('Enter a password: ')
    
    user = User(username, password, email)
    user_data.append({
            "username" : user.username,
            "password" : user.password,
            "email" : user.email
    })
    try:
        with open('users.json', 'w') as file:
            json.dump(user_data, file, indent=2)
    except FileNotFoundError:
        print('File not found!')
        quit()
    return "Account created successfully!"

def sign_in():
    username = input('Enter a username: ')
    
    for i in range(len(user_data)):
    
        if username == user_data[i]["username"]:
            password = input('Enter a password: ')
            if password == user_data[i]["password"]:
                AuthenticatedUser1.authenticated_user(username)
                return True
            else:
                while password != user_data[i]["password"]:
                    print("Incorrect password!")
                    password = input('Enter a password: ')
                AuthenticatedUser1.authenticated_user(username)
                return True   
    print('User not found! Make sure you have an account.')
    return -1