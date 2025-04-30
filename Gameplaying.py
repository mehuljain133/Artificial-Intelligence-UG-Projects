# Game Playing: introduction to game playing, min-max and alpha-beta pruning algorithms.

import math
import random

# --- Game Board ---
class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9  # 3x3 board

    def display(self):
        for i in range(3):
            print("|".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("-" * 5)

    def make_move(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    def is_winner(self, player):
        wins = [(0,1,2),(3,4,5),(6,7,8),
                (0,3,6),(1,4,7),(2,5,8),
                (0,4,8),(2,4,6)]
        return any(all(self.board[i] == player for i in combo) for combo in wins)

    def is_draw(self):
        return ' ' not in self.board and not self.is_winner('X') and not self.is_winner('O')

    def get_available_moves(self):
        return [i for i, val in enumerate(self.board) if val == ' ']

    def clone(self):
        clone = TicTacToe()
        clone.board = self.board[:]
        return clone

# --- Minimax Algorithm ---
def minimax(game, depth, maximizing_player):
    if game.is_winner('X'):
        return -10 + depth
    elif game.is_winner('O'):
        return 10 - depth
    elif game.is_draw():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in game.get_available_moves():
            new_game = game.clone()
            new_game.make_move(move, 'O')
            eval = minimax(new_game, depth + 1, False)
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = math.inf
        for move in game.get_available_moves():
            new_game = game.clone()
            new_game.make_move(move, 'X')
            eval = minimax(new_game, depth + 1, True)
            min_eval = min(min_eval, eval)
        return min_eval

# --- Alpha-Beta Pruning ---
def alpha_beta(game, depth, alpha, beta, maximizing_player):
    if game.is_winner('X'):
        return -10 + depth
    elif game.is_winner('O'):
        return 10 - depth
    elif game.is_draw():
        return 0

    if maximizing_player:
        max_eval = -math.inf
        for move in game.get_available_moves():
            new_game = game.clone()
            new_game.make_move(move, 'O')
            eval = alpha_beta(new_game, depth + 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break  # Prune
        return max_eval
    else:
        min_eval = math.inf
        for move in game.get_available_moves():
            new_game = game.clone()
            new_game.make_move(move, 'X')
            eval = alpha_beta(new_game, depth + 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  # Prune
        return min_eval

# --- AI Move Chooser using Minimax or Alpha-Beta ---
def best_move(game, player='O', use_alpha_beta=True):
    best_score = -math.inf
    best_move_found = None
    for move in game.get_available_moves():
        clone = game.clone()
        clone.make_move(move, player)
        if use_alpha_beta:
            score = alpha_beta(clone, 0, -math.inf, math.inf, False)
        else:
            score = minimax(clone, 0, False)
        if score > best_score:
            best_score = score
            best_move_found = move
    return best_move_found

# --- Play Game (Human vs AI) ---
def play_game():
    game = TicTacToe()
    current_player = 'X'  # Human goes first

    print("Tic-Tac-Toe (You = X, AI = O)")
    game.display()

    while True:
        if current_player == 'X':
            try:
                move = int(input("Enter your move (0-8): "))
                if game.make_move(move, 'X'):
                    current_player = 'O'
                else:
                    print("Invalid move. Try again.")
            except:
                print("Invalid input.")
        else:
            print("AI is thinking...")
            move = best_move(game, 'O', use_alpha_beta=True)
            game.make_move(move, 'O')
            current_player = 'X'

        game.display()

        if game.is_winner('X'):
            print("You win!")
            break
        elif game.is_winner('O'):
            print("AI wins!")
            break
        elif game.is_draw():
            print("It's a draw.")
            break

# --- Run Game ---
if __name__ == "__main__":
    play_game()
