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
