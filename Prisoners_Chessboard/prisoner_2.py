import save_chessboard_pdf as p
import numpy as np

# Simple Python script to take user input and display output

# Asking for user input
board_size = input("How many squares are on the board?")
heads_list = input("Enter the list of heads and tails as a binary string, starting from the top left corner")

# Displaying the output based on the user input
matrix = p.generate_connection_matrix(int(board_size))
colour = p.find_colour(heads_list, matrix)
print(f'The key is in position {colour}')

