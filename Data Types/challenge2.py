import os
from os import system
system('clear')




fname = input("What is your first name? >> ")
lname = input("What is your last name? >>  ")
age = int(input("What is your age? >> "))
gpa = float(input("What is your gpa? >> "))
email = input("What is your email address? >> ")

path = './log.txt'

def challenge():
    with open(path, 'a') as log:
        log.write(f'fname:       {fname}\nlname:       {lname}\nage:         {age}\ngpa:         {gpa}\nemail:       {email}')        
        log.close()





    

        
    


    

