# input row and coulmn number and output should be dynamic list
def dynamic_list(row, col):
    return [[0 for x in range(col)] for x in range(row)]
# test the function
# print(dynamic_list(100, 10))  # Output: [[0, 0,

# now want to print the list in a matrix form write the code for that

def print_matrix(matrix):
    for row in matrix:
        print(*row)

print_matrix(dynamic_list(2,3))

