import os
import sqlOPS as sql
from os import system
from user import User

system('clear')


users = []
def readUserOperation():
    sql.readUserInfo()

def insertOperation():
    numberOfEntries = int(input("Enter number of records >> "))
    for entry in range(numberOfEntries):
        print(f'--- User # {entry + 1} ---')
        user = User()
        fname = input("What is your first name? >> ")
        user.set_firstname(fname)
        lname = input("What is your last name? >>")
        user.set_lastName(lname)
        age = int(input("What is your age? >> "))
        user.set_age(age)
        phone = input("What is your phone number? >> ")
        user.set_phone(phone)
        users.append(user)
        print()
    for user in users:
        sql.insertUserInfo(user.get_firstname(), user.get_lastName(), user.get_age(), user.get_phone())

    readUserOperation()

def deleteOperation():
    sql.readUserInfo()
    userId = int(input("Which id do you want to delete? >> "))
    print("Thats ok")
    response = input("Are you sure? Y/N >> ")
    if response.upper() == 'Y':
        sql.deleteUser(userId)
    else:
        print("Thank you")
        sql.readUserInfo()
    
def updateOperation():
    sql.readUserInfo()
    user_id = int(input("Which id do you want to update? >> "))
    print("Alright")
    while True:
        field = input("What field would you like to update?")
        if field == "firstname":
            fname = input("What would you like to change the first name to? >> ")
            sql.updateUser(user_id.user_firstname(fname))
        else:
            print("Goodbye")
