''' This module finds the longest incremental path in a 2D matrix'''


input_matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
output = 4
print(f'Expected Count::{output}')


def row_wise():
    ''' Finding the incremental path in each row '''
    row_list = []
    for row in input_matrix:
        descend = {}
        ascend = {}
        for col in range(len(row)-1):
            if row[col] > row[col+1]:
                descend[row[col]] = col
                descend[row[col+1]] = col+1
            elif row[col] < row[col+1]:
                ascend[row[col]] = col
                ascend[row[col+1]] = col+1
        if descend:
            row_list.append(descend)
        if ascend:
            row_list.append(ascend)
    return row_list


def col_wise(row_list):
    ''' Finding the incremental path in each coloumn using index of maximun value from row '''
    incremental_path = 0
    for row_dict in row_list:
        count = len(row_dict.items())
        col = row_dict[max(row_dict.keys())]
        for row in range(1, len(input_matrix)):
            if input_matrix[row][col] > max(row_dict.keys()):
                count += 1
        if count > incremental_path:
            incremental_path = count
        return incremental_path


def main():
    row_list = row_wise()
    incremental_path_count = col_wise(row_list)
    print(f'Actual Count :: {incremental_path_count}')

main()
