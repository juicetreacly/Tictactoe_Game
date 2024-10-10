import numpy as np
from random import choice as random_choice

def print_board(matrix):
    """Displays the current state of the board."""
    symbol_map = {1: 'O', -1: 'X', 0: ' '}
    for row in matrix:
        print("|".join([symbol_map[val] for val in row]))
        print("-" * 5)

def human_move(matrix):
    """Takes input from the human player for their move."""
    while True:
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
            if matrix[row, col] == 0:
                return row, col
            else:
                print("This spot is already taken. Choose another.")
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

def get_next_turn(active_turn):
    """Switches turn between 1 (O) and -1 (X)."""
    return -active_turn

def score(matrix, player, depth):
    """Returns the score of the game state."""
    points = 10
    status = game_status(matrix)
    if status == 0:
        return 0  # draw
    if status == player:
        return points - depth  # player win
    return depth - points  # opponent win

def get_childs(matrix, turn):
    """Generates all possible child boards from the current board."""
    childs = []
    for i in range(3):
        for j in range(3):
            if matrix[i, j] == 0:
                child = matrix.copy()
                child[i, j] = turn
                childs.append(child)
    return childs

def game_status(matrix):
    """Checks the current state of the board."""
    for i in range(3):
        if np.all(matrix[i, :] == 1) or np.all(matrix[:, i] == 1):
            return 1  # O wins
        if np.all(matrix[i, :] == -1) or np.all(matrix[:, i] == -1):
            return -1  # X wins
    if matrix[0, 0] == matrix[1, 1] == matrix[2, 2] != 0:
        return matrix[0, 0]  # Diagonal win
    if matrix[0, 2] == matrix[1, 1] == matrix[2, 0] != 0:
        return matrix[0, 2]  # Anti-diagonal win
    return 0  # No winner yet

def game_over(matrix):
    """Checks if the game is over."""
    status = game_status(matrix)
    if status != 0 or np.all(matrix != 0):
        return True, status  # Game is over
    return False, status

def maximize(matrix, active_turn, player, depth, alpha, beta, nodes_visited):
    """Maximizing player."""
    game_finished, _ = game_over(matrix)
    if game_finished:
        return None, score(matrix, player, depth), nodes_visited
    depth += 1
    maxUtility = -np.inf
    best_move = None
    childs = get_childs(matrix, active_turn)
    for child in childs:
        nodes_visited += 1
        _, utility, nodes_visited = minimize(child, get_next_turn(active_turn), player, depth, alpha, beta, nodes_visited)
        if utility > maxUtility:
            best_move = child
            maxUtility = utility
        alpha = max(alpha, utility)
        if beta <= alpha:
            break  # Beta cut-off
    return best_move, maxUtility, nodes_visited

def minimize(matrix, active_turn, player, depth, alpha, beta, nodes_visited):
    """Minimizing player."""
    game_finished, _ = game_over(matrix)
    if game_finished:
        return None, score(matrix, player, depth), nodes_visited
    depth += 1
    minUtility = np.inf
    best_move = None
    childs = get_childs(matrix, active_turn)
    for child in childs:
        nodes_visited += 1
        _, utility, nodes_visited = maximize(child, get_next_turn(active_turn), player, depth, alpha, beta, nodes_visited)
        if utility < minUtility:
            best_move = child
            minUtility = utility
        beta = min(beta, utility)
        if beta <= alpha:
            break  # Alpha cut-off
    return best_move, minUtility, nodes_visited

def minimax(matrix, player):
    """Starts the minimax algorithm."""
    alpha = -np.inf
    beta = np.inf
    best_move, best_score, nodes_visited = maximize(matrix, player, player, 0, alpha, beta, 0)
    return best_move, best_score, nodes_visited

def run_game():
    """Main game loop."""
    board = np.zeros((3, 3), dtype=int)  # Empty 3x3 board
    current_turn = random_choice([1, -1])  # Randomize first player (O or X)

    print(f"Player 'O' is 1, Player 'X' is -1. Player '{'O' if current_turn == 1 else 'X'}' starts.")
    while True:
        print_board(board)
        if current_turn == 1:
            print("Human player's turn (O)")
            row, col = human_move(board)
            board[row, col] = current_turn
        else:
            print("AI player's turn (X)")
            best_move, _, _ = minimax(board, current_turn)
            board = best_move
        
        game_finished, status = game_over(board)
        if game_finished:
            print_board(board)
            if status == 1:
                print("Player 'O' wins!")
            elif status == -1:
                print("Player 'X' wins!")
            else:
                print("It's a draw!")
            break
        
        current_turn = get_next_turn(current_turn)

if __name__ == "__main__":
    run_game()
