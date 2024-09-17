from dicebase import Dice


class DiceDLX(Dice): # this is a subclass note: python does support multiple inheritance comma separated
    def __init__(self,face_value = 6 ):
        super().__init__(face_value) # pass args to base class
        # Dice.__init__(self,face_value) # this accomplishes the same thing as above, use this with multiple inheritance
        # self.dice_stats = [0,0,0,0,0,0]
        self.__dice_stats = [0] * 6  # same as above but easier, inits all elements to zero

    def update_stats(self):
        self.dice_stats[self.face_value - 1] += 1

    def roll(self):
        super().roll()
        self.update_stats()
        return self.face_value

    def draw(self):
        print("-----")
        print("|", self.face_value, "|")
        print("-----")

    @property
    def dice_stats(self):
        return self.__dice_stats

    @dice_stats.setter
    def dice_stats(self, new_value):
        pass