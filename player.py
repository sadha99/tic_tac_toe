import math
import random


class Player:

    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class HumanPlayer(Player):

    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input("Enter a nuber from (0-8) : ")
            try:
                val = int(square)
                if val not in game.available_moves():

                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square number , try again : ")
        return val


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):

        # just a random valid spot

        square = random.choice(game.available_moves())
        return square
