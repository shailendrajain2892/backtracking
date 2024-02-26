
def isSafe(i, j, N, maze):
    return i<N and j<N and maze[i][j]

def rat_in_a_maze_recur(i, j, maze, N, sol):
    if i == N-1 and j == N-1:
        sol[i][j] = 1
        return True
    if isSafe(i, j, N, maze):
        for k in range(1, maze[i][j]+1):
            if rat_in_a_maze_recur(i, j+k, maze, N, sol):
                sol[i][j] = 1
                return True
            if rat_in_a_maze_recur(i+k, j, maze, N, sol):
                sol[i][j] = 1
                return True
        # sol[i][j] = 0
    return False
            

def rat_in_a_maze(N, maze):
    i = 0
    j = 0
    sol = [[0 for i in range(N)] for j in range(N)]
    if rat_in_a_maze_recur(i, j, maze, N, sol):
        print(sol)
    else:
        print(-1)

maze = [[2, 1, 1, 1], 
        [3, 0, 0, 1],
        [0, 1, 0, 1],
        [0, 0, 0, 1]]
rat_in_a_maze(4, maze)

# Input:
# N = 4
# maze[][] = {{2,1,0,0},{3,0,0,1},
# {0,1,0,1},{0,0,0,1}}
# Output:
# 1 0 0 0
# 1 0 0 1
# 0 0 0 1
# 0 0 0 1
# Explanation: Rat started with m[0][0] and
# can jump up to 2 steps right/down. First
# check m[0][1] as it is 1, next check
# m[0][2], this won't lead to the solution.
# Then check m[1][0], as this is 3(non-zero)
# so we can make 3 jumps to reach m[1][3].
# From m[1][3] we can move downwards taking
# 1 jump each time to reach destination at
# m[3][3]. 