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
        square = random.choice(game.available_moves())
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
                if(val not in game.available_moves()):
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again")
    
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_move(self, game):
        if len(game.available_moves()) == 0:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {"position": None,
                    'score': 1 * (state.num_empty_squares() +1) if other_player == max_player else -1 * (state.num_empty_squares() +1) }
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position':None, 'score':-math.inf}
        else:
            best = {'position':None, 'score':math.inf}

        for possible_move in state.available_moves():
            # Step 1: make a move, try that spot
            state.make_move(possible_move, player)

            # Step 2: recurs using minimax to simulate the other player
            sim_score = self.minimax(state, other_player)

            # Step 3: undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best

