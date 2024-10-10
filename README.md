# Tictactoe_Game
Tic-Tac-Toe with AI
# Overview
This is a simple Tic-Tac-Toe game built in Python, where the player competes against an AI opponent. The AI uses the Minimax Algorithm with alpha-beta pruning to make optimal moves. The human player always plays as 'O', and the AI plays as 'X'.

# The game features:

A 3x3 grid representing the Tic-Tac-Toe board.
Human player input via the terminal.
AI opponent that uses the Minimax algorithm to calculate its best moves.
Displays the game board after every move.
# How It Works
The game follows standard Tic-Tac-Toe rules:

Players take turns placing their mark ('O' for the human player, 'X' for the AI) on an empty cell.
The first player to align three of their marks in a row, column, or diagonal wins.
If the board is filled without any player winning, the game ends in a draw.
The AI uses the Minimax algorithm with alpha-beta pruning to explore all possible future moves and make the optimal choice.

# Getting Started
# Prerequisites
Ensure you have Python installed (version 3.x) on your system. You will also need the numpy library.

You can install numpy by running:

# bash
Copy code
pip install numpy
Running the Game
Clone or download the project files to your local machine.
Open a terminal and navigate to the project directory.
Run the game with the following command:
# bash
Copy code
python your_script_name.py
The game will display the board, and you'll be prompted to enter the row and column to place your move.
Controls
The board is a 3x3 grid with rows and columns indexed from 0 to 2.
When prompted, enter the row and column number (separated by prompts) to place your mark.
Example input:

markdown
Copy code
Player 'O' is 1, Player 'X' is -1. Player 'O' starts.
O| | 
-----
 | | 
-----
 | | 

Human player's turn (O)
Enter row (0, 1, or 2): 0
Enter column (0, 1, or 2): 0
The game will alternate between the human player's move and the AI player's turn, displaying the updated board after each move.

# How the AI Works
The AI uses the Minimax Algorithm with alpha-beta pruning:

It recursively evaluates all possible future moves and assigns a score to each board configuration.
The AI selects the move that maximizes its chances of winning while minimizing the human player's chances.
# License
This project is open source and available under the MIT License.
