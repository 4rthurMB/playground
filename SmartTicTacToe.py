# ----------------------------------
# Smart - Tic-Tac-Toe // PLAYER
# ----------------------------------

import random
import math

class Player:
    def __init__(self, letter):
        # letter is X or O
        self.letter = letter

    # We want all players to get their next move given a game
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8): ')
            # Check if the input is a valid integer
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid square. Try again.')
        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    # Function to choose the best move based on the minimax algorithm
    def get_move(self, game):
        # If the game is empty (not started), choose a random spot
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            # Get the square based on the minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square

    # Function to implement the minimax algorithm
    def minimax(self, round, player):
        max_player = self.letter  # Yourself
        other_player = 'O' if player == 'X' else 'X'  # The other player

        # First: Check if the previous move is a winner
        if round.current_winner == other_player:
            return {'position': None, 
                    'score': 1 * (round.num_empty_squares() + 1) if other_player == max_player else -1 * (round.num_empty_squares() + 1)}

        # If there are no winner but there are empty squares,
        # then we need to keep going 
        elif not round.num_empty_squares():
            return {'position': None, 'score': 0}

        # If its my turn, then we want to maximize the max_player
        # -math.inf is the worst case scenario for the max_player (minimum possible score)
        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # Each score should maximize (be larger)
        else: 
            best = {'position': None, 'score': math.inf}  # Each score should minimize (be smaller)

        for possible_move in round.available_moves():
            # Step 1: make a move, try that spot
            round.make_move(possible_move, player)
            # Step 2: recurse using minimax to simulate a game after making that move
            sim_score = self.minimax(round, other_player)  # Now, we alternate players
            # Step 3: undo the move
            round.board[possible_move] = ' '
            round.current_winner = None
            sim_score['position'] = possible_move  # This represents the move optimal next move
            # Step 4: update the dictionaries if necessary
            if player == max_player:  # We are trying to maximize the max_player and minimize the other player
                if sim_score['score'] > best['score']:
                    best = sim_score  # Replace best
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score  # Replace best
        return best