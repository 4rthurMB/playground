# ----------------------------------
# Smart - Tic-Tac-Toe // GAME
# ----------------------------------

from SmartTicTacToe import HumanPlayer, GeniusComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # A list to represent the board
        self.current_winner = None  # Keep track of the winner!

    def print_board(self):
        for rows in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(rows) + ' |')

    @staticmethod   # Used as a helper to functions that don't need to access the instance of the class
    def print_board_nums():
        # 0 | 1 | 2 etc (tells us what number correspods to what box)
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for rows in number_board:
            print('| ' + ' | '.join(rows) + ' | ')

    # Return a list of available moves (empty squares)
    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            # ['x', 'x', 'o'] --> [(0, 'x'), (1, 'x'), (2, 'o')]
            if spot == ' ':
                moves.append(i)
        return moves

    # Return a boolean indicating if there are empty squares on the board
    def empty_squares(self):
        return ' ' in self.board

    # Return the number of empty squares
    def num_empty_squares(self):
        return self.board.count(' ')

    # Check if the move is valid and then make it
    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            # Check if this move is a winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check the row, by getting the quotient (possible values : 0, 1, 2)
        row_ind = square // 3
        # Based on the row index, we get the row from the board
        row = self.board[row_ind*3:(row_ind+1)*3]
        # If all the spots in the row are the same letter, then we have a winner
        if all([spot == letter for spot in row]):
            return True

        # Check the column, by getting the remainder (possible values : 0, 1, 2)
        col_ind = square % 3
        # Based on the column index, we get the whole column from the board
        column = [self.board[col_ind+i*3] for i in range(3)]
        # If all the spots in the column are the same letter, then we have a winner
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals
        if square % 2 == 0:  # Only even squares are part of diagonals (0, 2, 4, 6, 8)
            diagonal1 = [self.board[i] for i in [0, 4, 8]]  # Left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]  # Right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board_nums()

    letter = 'X' # starting letter
    # iterate while the game still has empty squares
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter

            # Switch players
            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)