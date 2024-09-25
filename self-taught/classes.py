import csv
import os


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
