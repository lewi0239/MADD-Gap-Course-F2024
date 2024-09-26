import csv
import os

# https://realpython.com/python3-object-oriented-programming/


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

"""
class Stock:
    def __init__(self, symbol, price, sector):
        self.symbol = symbol
        self.price = price
        self.sector = sector


appl = Stock("AAPL", 1000, "tech")

print(appl.symbol)
print(appl.price)
print(appl)


# Get stock name and price from user input
stock_builder_name = input("Please enter stock Name: ")
# assuming price is a number
stock_builder_price = float(input("Please enter stock Price: "))

# Define a class to represent a stock


class Stock_Build:
    def __init__(self, stock_builder_name, stock_builder_price):
        self.stock_builder_name = stock_builder_name
        self.stock_builder_price = stock_builder_price

    # Adding a method to print the stock information
    def __repr__(self):
        return f"Stock Name: {self.stock_builder_name}, Stock Price: {self.stock_builder_price}"


# Create an instance of Stock_Build
bro = Stock_Build(stock_builder_name, stock_builder_price)

# Print the created object, which will call the __repr__ method
print(bro)
"""


class File:
    is_password_protected = False

    def __init__(self, file_type: str, size: int, dir: str, department: str):
        self.type = file_type
        self.size = size
        self.dir = dir
        self.department = department

    def __repr__(self):
        return f"File Type: {self.type}, File Size: {self.size}, File Directory: {self.dir}"


csv_report = File('excel-sheet', 4331,
                  'c:\\Users\\Documents\\Accounting', "accounting")


print(csv_report)


class Dog:
    species = "Canis familiaris"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


"""
Creating a new object form a class is called instatniating a class. You can create a new object by typing the nameof the class, followed by opening and closing parentheses:
"""

Dog("billy", 5)
Dog("danny", 3)
Dog('Don', 7)

"""
The enw Dog istnace is located at a different memory address. That's because it's entirely new instance and is completely unique from the first Dog object that you created.

To see this another way:
"""


a = Dog("A", 33)
b = Dog("B", 33)
c = Dog("C", 33)

a == b


Miles = Dog("Miles", 4)

print(Miles.age)

print(Miles.name)

print(Miles.species)


# Instantiate Classes

class Dog:
    pass


Dog()  # Dog object at 0x1023213d30> (made up memory location)


# Python obhject stores the Dog object in your computers memory.


# Python inheritance from another class

"""
Inheritance is the process by which one class takes on the atrributes and methods of another. Newly formed classes are called child classes, and the classes tht you derive child classes from are called parent classes

You inherit from a parent class by creating a new class and putting the name of the parent class into parentheses:

"""

# main class


class Parent:
    hair_color = "brown"
    speaks = ["English"]

# new class inheriting the main class


class Child(Parent):
    def __init__(self):
        super().__init__()
        self.speaks.append("French")


print(Child.hair_color)  # brown

"""
Child classes can override or extend the attributes and methods of parent classes. In other words, child classes inherit all of the parent’s attributes and methods but can also specify attributes and methods that are unique to themselves.




You may have inherited your hair color from your parents. It’s an attribute that you were born with. But maybe you decide to color your hair purple. Assuming that your parents don’t have purple hair, you’ve just overridden the hair color attribute that you inherited from your parents:`
"""


Child.hair_color = "purple"

"""
By instantiating the Child class with child_instance = Child(), you trigger the __init__() method, which appends "French" to the speaks list.

"""

# make Car class:


class Car:
    number_of_doors = 4
    car_list = []

    def __init__(self, price: int, year: int, make: str):
        self.price = price
        self.year = year
        self.make = make

        Car.car_list.append(self)

    def __str__(self):
        return f'The {self.year} {self.make} is ${self.price}'

    def country(self, location):
        return f'{self.make} is made in {location}'


# Create instances of Car
BMW = Car(50000, 2023, "BMW")
audi = Car(55000, 2022, "Audi")
ford = Car(65000, 2017, "Ford")

print(BMW.country("Germany"))


for car in Car.car_list:
    print(car)

for car in Car.car_list:
    print(car.make + " has " + str(car.number_of_doors) + " doors")


class Truck(Car):
    truck_bed_size_feet = 10


yellow_truck = Truck(12500, 2011, "")


"""
The super() function does much more than just search the parent class for a method or an attribute. It traverses the entire class hierarchy for a matching method or attribute. If you aren’t careful, super() can have surprising results.
"""
"""
Conclusion
In this tutorial, you learned about object-oriented programming (OOP) in Python. Most modern programming languages, such as Java, C#, and C++, follow OOP principles, so the knowledge that you gained here will be applicable no matter where your programming career takes you.

In this tutorial, you learned how to:

Define a class, which is a sort of blueprint for an object
Instantiate a class to create an object
Use attributes and methods to define the properties and behaviors of an object
Use inheritance to create child classes from a parent class
Reference a method on a parent class using super()
Check if an object inherits from another class using isinstance()

"""
