import numpy as np
import matplotlib.pyplot as plt
from matplotlib.table import Table
import sys

def generate_connection_matrix(board_size): 

    connection_matrix = np.zeros((board_size, board_size))
    nums = list(range(1, board_size + 1))
    
    connection_matrix[0] = nums # creating 1st row
    for row in nums:
        for col in nums:
            allowed_nums = list(range(1, board_size + 1))
            if connection_matrix[row - 1][col - 1] == 0: 
                # Checking the numbers already in this row and removing them from allowed nums
                for num in connection_matrix[row - 1]:
                    if num in allowed_nums: allowed_nums.remove(num)
                
                # Checking the numbers already in this column
                for num in [connection_matrix[_][col - 1] for _ in range(board_size)]:
                    if num in allowed_nums: allowed_nums.remove(num)
                
                connection_matrix[row - 1][col - 1] = allowed_nums[0]
                

    return connection_matrix.astype(int)

def flip_nth_bit(n, binary_num):
    binary_list = list(binary_num)
    binary_list.reverse()
    if binary_list[n] == '0':
        binary_list[n] = '1'
    else:
        binary_list[n] = '0'
    binary_list.reverse()
    return ''.join(binary_list)

def generate_hypercube_vertices(dimension):
    vertices = []
    def genbin(n, bs=''):
        if len(bs) == n:
            vertices.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')

    genbin(dimension)
    return vertices

def find_1s(binary_string):
    binary_list = list(binary_string)
    binary_list.reverse()
    idxs = []
    for char in binary_list:
        if char == "1":
            idx = binary_list.index(char)
            idxs.append(idx)
            binary_list[idx] = 0
    return idxs

def colour_vertices(connection_matrix):
    dimension = len(connection_matrix)
    vertices = generate_hypercube_vertices(dimension)
    colours = []

    for vertex in vertices:
        flipped_dimensions = find_1s(vertex)
        colour = 0
        for dim in flipped_dimensions:
            new_colour = int(connection_matrix[dim][colour])
            colour = new_colour
        colours.append(colour)
    
    hypercube = {}
    n = 0 
    for vertex in vertices:
        hypercube[vertex] = colours[n]
        n+=1
    return hypercube

def find_colour(heads_list, connection_matrix):
    flipped_dimensions = find_1s(heads_list)
    colour = 0
    for dim in flipped_dimensions:
        new_colour = int(connection_matrix[dim][colour])
        colour = new_colour
    return colour

def flip_this_coin(key_position, heads_list, connection_matrix):
    current_colour = find_colour(heads_list, connection_matrix)
    column = [connection_matrix[_][current_colour] for _ in range(len(connection_matrix))]
    flip_dimension = column.index(key_position)

    return flip_dimension



def make_table(connection_matrix, name):
    matrix = connection_matrix

    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(11.7, 8.3))  # A4 size in inches (landscape)

    # Hide the axes
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.set_frame_on(False)

    # Create a table
    table = Table(ax, bbox=[0, 0, 1, 1])

    # Add data to the table
    nrows, ncols = matrix.shape
    for i in range(nrows):
        for j in range(ncols):
            table.add_cell(i, j, 1/ncols, 1/nrows, text=f'{matrix[i, j]}', loc='center', edgecolor='black')

    # Add the table to the plot
    ax.add_table(table)

    # Save the figure to a PDF
    plt.savefig(f'{name}.pdf', bbox_inches='tight', pad_inches=0.1, dpi=300)

###################################################################################################################################

def main():

    board_size = 16
    board_name = '16x16'
    assert board_size % 2 == 0

    conn_mat = generate_connection_matrix(board_size) 

    make_table(conn_mat, board_name)

###################################################################################################################################
if __name__ == "__main__":
    sys.exit(main())