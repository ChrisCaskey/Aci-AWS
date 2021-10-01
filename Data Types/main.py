import os
from os import system
system("clear")
from person import Person


path = './log.txt'

numberOfPersons = int(input("Enter how many People would you like to add? >>"))
people = []

def printObjects(p):
    person_counter = 1
    print()
    print("This is your personnel info:")
    for persons in p:
        print(f'''
        Person # {person_counter}
        First Name: ........ {person.get_fname()}
        Last Name: ....... {person.get_lname()}
        Email: ....... {person.get_email()}
        Phone #: ....... {person.get_phone()}
        ''')

        person_counter += 1
    
   


for index in range(numberOfPersons):
    person = Person()
    print()
    print("**********************************")
    print("********* Person # ", index + 1, "**********")
    print("**********************************")
    fname = input("What is your first name? >>")
    person.set_fname(fname)
    lname = input("What is your last name> >>")
    person.set_lname(lname)
    email = input("What is your email? >>")
    person.set_email(email)
    phone = int(input("What is your phone number? >>"))
    person.set_phone(phone)
    people.append(person)
    with open(path, 'a') as log:
        log.write(f'fname:       {fname}\nlname:       {lname}\nemail:         {email}\nphone:         {phone}')        
        log.close()



printObjects(people)



