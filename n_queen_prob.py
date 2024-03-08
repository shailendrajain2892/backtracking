import sys


def isSafe(row, col, mat, n):
    # traverse left and right
    for j in range(col):
        if mat[row][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if mat[i][j]:
            return False
    for i, j in zip(range(row, n), range(col, -1, -1)):
        if mat[i][j]:
            return False
    return True

    

def find_co_ordinates(col, mat, n):
    if col == n:
        return True
    for i in range(n): 
        if isSafe(i, col, mat, n):
            mat[i][col] = 1
            if find_co_ordinates(col+1, mat, n):
                return True
            mat[i][col] = 0
    return False

def n_queen_prob(n):
    mat = [[0 for i in range(n)] for j in range(n)]
    if find_co_ordinates(0, mat, n):
        print(mat)
        return True
    else:
        return False

print(n_queen_prob(int(sys.argv[1])))