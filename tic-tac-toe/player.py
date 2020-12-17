import math 
import random

# Base player class
class Player:
    def __init__(self, letter):
        # Letter is x or o
        self.letter = letter
    
    # Given a game, all players must get their next move
    def get_move(self, game):
        pass

# JS Equivalent: RandomComputerPlayer extends Player
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.avaliable_moves())
        return square

class HumanPlayer(Player):
    # Basically, pass the letter to the constructor of player
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):   
        valid_square = False
        val = None
        while not valid_square:
            square = input(f"{self.letter}'s turn. Input move (1-9): ")
            # Checks if move is allowed

            try:
                val = int(square)
                val = val-1
                if(val not in game.avaliable_moves()):
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again")
    
        return val
