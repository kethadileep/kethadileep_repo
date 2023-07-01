''' This module rotates the 2D matrix by 90 degrees right '''

# input_matrix = [[1,2,3],[4,5,6],[7,8,9]]
# output = [[7,4,1],[8,5,2],[9,6,3]]

input_matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

print('Expected_matrix::', output)

input_matrix_length = len(input_matrix)

for column in range(input_matrix_length):
    input_matrix.append([])
    new_row = input_matrix[-1]
    for row in range(input_matrix_length-1, -1, -1):
        new_row.append(input_matrix[row][column])

del input_matrix[:input_matrix_length]
print('Rotated_matrix ::', input_matrix)
