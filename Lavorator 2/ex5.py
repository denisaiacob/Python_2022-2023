'''
Write a function that receives as parameter a matrix and will return the matrix
obtained by replacing all the elements under the main diagonal with 0 (zero).
'''


def replacing_under_diagonal(matrix):
    for i in range(1, len(matrix)):
        for j in range(0, i):
            matrix[i][j] = 0
    return matrix


if __name__ == '__main__':
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(replacing_under_diagonal(matrix))
