import math
import time
from player import HumanPlayer
from player import RandomComputerPlayer


class TicTacToe:
    def __init__(self):
        self.board = self.make_board()
        self.currentWinner = None

    @staticmethod
    def make_board():

        # using a single line to represent a 3x3 board
        return ['-' for i in range(9)]

    def print_board(self):  # printing an empty tic tac toe board
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # this will return the indexes
        return [i for (i, spot) in enumerate(self.board) if spot == '-']

        # enumerate will return a tuples of the index and the value
        # [x,x,o] -> [(0,x) ,(1,x),(2,o) ]

        # for (i, spot) in enumerate(self.board):
        #     if spot == ' ':
        #         moves.append[i]
    def empty_squares(self):
        return ' ' in self.board  # this will return a boolean value

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if move is valid, make the move, assign the letter to the square, return true,
        # if move is invalid, return false

        if self.board[square] == '-':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentWinner = letter
            return True
        return False

    def winner(self, square, letter):
        # check all rows
        row_ind = square//3  # floor of square / 3 which will give the row index

        row = self.board[row_ind*3:(row_ind+1)*3]

        col_ind = square % 3

        col = [self.board[col_ind+i*3] for i in range(3)]

        diagnal1 = [self.board[i] for i in (0, 4, 8)]

        diagnal2 = [self.board[i] for i in (2, 4, 6)]

        if all(s == letter for s in row):
            return True
        if all(s == letter for s in col):
            return True
        # the only possible value of diagnols are [0,2,4,6,8]
        if square % 2 == 0:
            if all(s == letter for s in diagnal1):
                return True
            if all(s == letter for s in diagnal2):
                return True
        


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X'  # starting letter
    # keep iterating until the game has a winner

    while game.empty_squares:
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} made a move to {square} ")
                game.print_board()

                print(" ")

            if game.currentWinner:
                if print_game:
                    print(f"{letter} is the winner !")
                return letter
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It is a tie! ")

if __name__ == "__main__":
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, True)
