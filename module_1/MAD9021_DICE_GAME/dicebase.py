import random
import uuid


class Empty:
    pass    # this prevents an error, python just ignores the issue because of pass


# our base or super class NOTE: python uses super to access base class
class Dice:
    # __face_value = 1  #  class variable/attribute can access like static using class name: Dice.__face_value
    # or just for the instance using self.__face_value, which creates a local instance of this variable

    def roll(self):
        self.__face_value = random.randint(1,6)
        return self.__face_value

    def draw(self):
        print(self.__face_value)

    def __init__(self,face_value = 1):
        if 0 < face_value < 7: # Simplify Chained Comparison
            self.__face_value = face_value
        else:
            self.__face_value = 1
        random.seed(int(str(uuid.uuid4())[:8], 16)) # make a random UUID

    @property
    def face_value(self):
        return self.__face_value

    @face_value.setter
    def face_value(self, face_value):
        if  0 < face_value < 7: # Simplified Chained Comparison
            self.__face_value = face_value













