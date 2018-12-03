m, n = (int(i) for i in input().split())
matrix = [[None for i in range(n)] for i in range(m)]
for i in range(int(input())):
    i, j = (int(i) - 1 for i in input().split())
    matrix[i][j] = '*'

for i, row in enumerate(matrix):
    for j, elem in enumerate(row):
        if not elem:
            near_bombs = 0
            for idx_1 in [-1, 0, 1]:
                for idx_2 in [-1, 0, 1]:
                    try:
                        if (matrix[i + idx_1][j + idx_2] == '*' and
                           (idx_1 or idx_2) and i + idx_1 >= 0 and
                           j + idx_2 >= 0):
                            near_bombs += 1
                    except IndexError:
                        pass
            matrix[i][j] = near_bombs

for row in matrix:
    print(*row)
