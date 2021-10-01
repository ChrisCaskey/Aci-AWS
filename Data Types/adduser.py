import os
from os import system
system("clear")

def createUser():
    username = str(input("Enter a username >> "))
    system(f"sudo useradd {username}")

createUser()