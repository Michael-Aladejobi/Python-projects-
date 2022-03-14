import random


class Dice:
    def roll():
        first_die = random.randint(1,6) #a random class method that generates a random number between 1 and 6 inclusively.
        second_die = random.randint(1,6) #same as the first die
        return first_die, second_die


dice = Dice()
print(dice.roll())
