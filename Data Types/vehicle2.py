import os
from os import system
system("Clear")
from vehicle import Car


cars = []

numberOfCars = int(input("Enter how many cars you want to purchase >>"))

print("You have chosen to enter", numberOfCars, "cars")

for index in range(numberOfCars):
    cars = Car()
    print()
    print("**********************************")
    print("******* CAR # ", index + 1, "************")
    print("**********************************")
    make = input("What is the make? >>")
    Car.setMake(make)
    model = input("What is the model? >>")
    Car.setModel(model)
    year = input("What is the year? >>")
    Car.setYear(year)
    color = input("What is the color? >>")
    Car.setColor(color)
    price = float(input("What is the Price? >>"))
    Car.setPrice(price)
    trim = input("What is the trim? >>")
    Car.setTrim(trim)
    Car.append(cars)


def printObjects(c):
    car_counter = 1
    print()
    print("This is your purchase info:")
    for car in c:
        print(f'''
            Car # {car_counter}
            Make: ........ {cars.getMake()}
            Model: ....... {cars.getModel()}
            Year: ....... {cars.getYear()}
            Color: ....... {cars.getColor()}
            Trim: ....... {cars.getTrim()}
            Price: ....... {cars.getPrice()}
            ''')

        car_counter += 1