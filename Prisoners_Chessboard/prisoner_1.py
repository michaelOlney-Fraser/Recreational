import save_chessboard_pdf as p

print("The warden has set the board: Prisoner 1 enters the room and sees it.")

board_size = input("How many squares are on the board? ")
heads_list = input("Enter the list of heads and tails as a binary string, starting from the top left corner ")
key_position = input("Enter the key position as an integer from 0 to the number of squares on the board minus 1 ")

matrix = p.generate_connection_matrix(int(board_size))
flip = p.flip_this_coin(int(key_position), str(heads_list), matrix)
nb = p.flip_nth_bit(flip, heads_list)

# Displaying the output based on the user input
print(f'You have to flip the coin at position: {flip}, the new configuration will be {nb}')

question = input("Prisoner 1 should leave the room, press enter and leave")

print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")

pris_2_board  = input('Prisoner 2 enters the room and sees the board, what is the current board position?')

key_position_final = p.find_colour(pris_2_board, matrix)

print(f'Based on this, you should check under position {key_position_final}')