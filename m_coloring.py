import sys


def isSafe(node, color, V, graph, color_list):
    for j in range(V):
        if graph[node][j] and color_list[j] == color:
            return False
    return True
        
            

def checkifColorPossible(graph, k, V, node, colors):
    if node == V:
        return True
    for col in range(1, k+1):
        if isSafe(node, col, V, graph, colors):
            colors[node] = col
            if checkifColorPossible(graph, k, V, node+1, colors):
                return True
            colors[node] = 0
    return False
    
#Function to determine if graph can be coloured with at most M colours such
#that no two adjacent vertices of graph are coloured with same colour.
def graphColoring(graph, k, V):
    colors = [0]*V
    #your code here
    if checkifColorPossible(graph, k, V, node=0, colors=colors):
        return True
    else:
        return False

k=int(sys.argv[1]) # no of colors
V=4 # no of verticies 
graph = [[0, 1, 1, 1], [1, 0, 0, 1], [1, 0, 0, 1], [1, 1, 1, 0]]
print(graphColoring(graph, k, V))