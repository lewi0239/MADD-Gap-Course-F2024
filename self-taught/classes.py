class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


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
