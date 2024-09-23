import os
# input example
name = input("Please provide me your name: ")

print("Your name is " + name)

formula = input("Enter operation (1: add, 2: subtract): ")


a = int(input("Enter in number one: "))
b = int(input("Enter in number two: "))

match formula:
    case "1":
        print(a+b)
    case "2":
        print(a-b)
    case _:
        print("Unkown operations")


def calculate_future_value(pv, r, n, t):
    fv = pv * (1 + r / n) ** (n * t)
    return fv


pv = int(input("please enter present value for investment"))
r = int(input("please enter rate of investment"))
n = int(input("please enter present number of times it compounds per year"))
t = int(input("please enter number of years for investment"))

fv = calculate_future_value(pv, r, n, t)

print(f"The future value of the investment is: ${fv:.2f}")
