import os 
from os import system
system('clear')

bananas= int(input("How many bananas do you have? >>"))
while True:
    if bananas < 0:
        print("What in the world is this number?")
        print("Please try again")
        bananas= int(input("How many bananas do you have? >>"))
    else:
        break
if bananas >= 5:
            print("I have a large bunch of bananas")
elif bananas >= 1 and bananas <= 4:
        print("I have a small bunch of bananas")
else:
        print("I dont have any bananas")
