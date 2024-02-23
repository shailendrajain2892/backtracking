from pprint import pprint


def isSafe(i, j, maze, N):
    return i < N and j < N and maze[i][j]

def solveMazeRecur(i, j, maze, sol, N):
    if i ==  N-1 & j == N-1 :
        sol[i][j] = 1
        return True
    if isSafe(i, j, maze, N):
        if solveMazeRecur(i+1, j, maze, sol, N):
            sol[i][j] = 1
            return True
        elif solveMazeRecur(i, j+1, maze, sol, N):
            sol[i][j] = 1
            return True
        sol[i][j] = 0
    return False

def solveMaze(maze):
    sol = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    if solveMazeRecur(0, 0, maze, sol, 4):
        print(sol)
        return True
    else:
        return False    
maze = [[1, 0, 0, 0],
[1, 1, 0, 1],
[0, 1, 0, 0],
[1, 1, 1, 1]]
pprint(solveMaze(maze))
