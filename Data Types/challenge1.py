import os 
from os import system
system('clear')

#Non fruitful function

def printName():
    print("My name is Charles")


printName()


def printInfo(name, age):
    print(f"My name is {name} and I am {age} years old")

printInfo("Charles", 30)

def printInfoNoArgs():
    return "I am happy to be here"

string = printInfoNoArgs()
print(string)

def printinfowithargs(price):
    tax = price * 0.07
    subtotal = price
    grandtotal = price + tax
    return tax, subtotal, grandtotal

print(printinfowithargs(2499))


t, sbtotal, gtotal = printinfowithargs(2499)
print(f'''
    Tax:........... ${t}
    subtotal:...... ${sbtotal}
    grandtotal:.... ${gtotal}
''')


