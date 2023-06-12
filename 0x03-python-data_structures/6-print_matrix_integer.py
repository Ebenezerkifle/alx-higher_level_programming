#!/usr/bin/python3
def print_matrix_integer(matrix = [[]]):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if(len(matrix[i]) == j + 1 and len(matrix) == i + 1):
                print('{:d}'.format(matrix[i][j]), end="")
            elif(len(matrix[i]) == j + 1):
                print('{:d}'.format(matrix[i][j]), end="$\n")
            else:
                print('{:d}'.format(matrix[i][j]), end=" ")
    print("$")
