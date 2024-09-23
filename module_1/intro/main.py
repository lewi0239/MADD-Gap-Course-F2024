

import os
user_name = "brodie"

print(user_name)

# function for python


def func():
    print('this is a test function')


print(func)


text = "Here Is somE TeXt"
# console log text
print(text.upper())
print(text.title())
print(text[0:4].upper())
print(text[0:4].upper())
print(text[6:].upper())  # Start at 6 to the end


print(text.count('E'))

print(text.find('m'))

numbers = [11, 2, 3, 5, 6, 7, 8]

print(min(numbers))
print(max(numbers))
print(sum(numbers))


# loops  - 2 types - for loop and while loop
for value in numbers:
    print(value)


# get index

for index, value in enumerate(numbers):
    print(index, ': ', value)


# Use a range

for i in range(5, 10):  # inclusive, exclusive
    print(i)


# coniditon statements:

the_cheese = 'swiss'

if the_cheese == 'cheddar':
    print(the_cheese)
elif the_cheese == 'blue':
    print('Yummy blue cheese')
else:
    print('Your cheese is unknown!')

# Supports < >

have_cheese = False

if have_cheese:
    print("Yum!")


if not have_cheese:
    print('sad no cheese')


# Importing


print(os.getcwd())


# dunder variables and dunder methods

print(__name__)
print(__file__)

if __name__ == 'main':
    print('this file is named main.py')

<< << << < HEAD
test = True

print(test)
== == == =

# Module one and two debrief:

# Data Types:

# Numeric 3x

# 1. Integer
my_age = 31
# 2. Float
market_value_per_share = 15
eps = 3.75
price_earning_ratio = market_value_per_share / eps
print(price_earning_ratio)
# 3. Complex
compound_c = 3+4j


# Sequence 4x
# 1. Strings
my_name = 'brodie'

# f strings (template literals in javascript)
print(f"Hello my name is {my_name}")

# 2. Lists
todo_list = ['workout', 'study', 'read']

# 3. Tuples
movie_start_times = (1300, 1630, 1900, 2200)

# 4. Range
daily_tempature = range(-3, 23)

# Maps 1x (in this example shows a list of dictionaries, same as an array of objects in JavaScript)
my_friends = [{"name": "Tom", "age": 31},
              {"name": "Alice", "age": 25}]
# sets 2x
# 1. Set
locations = {"Ottawa", "Montreal", "Toronto"}
# 2. Frozenset
locations_continent = frozenset({"North America"})
# Binary 3x

# 1. Bytes immutable
message = b"hello"
# 2. Bytearray mutable
todays_date = bytearray(b"Monday")

# 3. Memoryview
memoryview(b"Hello")
# None 1x
# 1. NoneType (absence of a value)
no_value = None
# total types = 15

# functions


def greet(name):
    print(f"Hello, {name}")
    return name
