from dicebase import Dice
from diceDLX import DiceDLX
import time

dice = Dice()

for index in range(10):
    print(dice.roll(), end=",")

print()

dice2 = Dice(6)

for index in range(10):
    print(dice2.roll())

dlx1 = DiceDLX()

dlx1.draw()

start_time = time.time()
for i in range(1,600000):
    dlx1.roll()
end_time = time.time()

print("total time taken this loop: ", end_time - start_time)

# dlx1.dice_stats = None

print(dlx1.dice_stats)

# print(help(DiceDLX)) # Method resolution order is displayed

# python helper functions:

# print("This is an instance: ", isinstance(dice2, Dice)) # is dice2 an instance of Dice class
# print("This is an instance: ", isinstance(dice2, DiceDLX)) # is dice2 an instance of DiceDLX class
#
# print("This is an instance: ", isinstance(dlx1, DiceDLX)) # is dlx1 an instance of DiceDLX class
# print("This is an instance: ", isinstance(dlx1, Dice)) # is dlx1 an instance of Dice class, True due to inheritance
#
# print("This is a subclass: ", issubclass(DiceDLX, Dice)) # is DiceDLX a subclass of Dice = True
# print("This is a subclass: ", issubclass(Dice , DiceDLX)) # is Dice a subclass of DiceDLX = False

