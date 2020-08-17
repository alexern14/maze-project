import numpy as np
import calcAdjacencies
import calcAdjacenciesDiagnol
import calcGRAPH

def printPath(path):
    for item in path:
        print((item[0] + 1, item[1] + 1, item[2]), end=" ")
    print("\n")
    for item in path:
        print((item[0] + 1, item[1] + 1), end=" ")
    exit()

def DFS(graph, start, visited, done, path):
    if visited is None:
        visited = []
    if start in visited:
        return
    visited.append(start)
    if start == [7, 7, 1]:
        printPath(visited)
    if start == [7, 7, 0]:
        printPath(visited)
    NEXT = graph[tuple(start)]
    for next in NEXT:
        DFS(graph, next, visited, done, path)
    visited.pop()
    return path

#Read in file
file = open("maze.txt", "r")
rows_columns = file.readline()
split = rows_columns.split()

num_rows = int(split[0])
num_columns = int(split[1])

maze = []
coor = []

ROW = 0
for line in file:
    line = line.split()
    if line:
        line = [int(i) for i in line]
        maze.append(line)
        COLUMN = 0
        for i in line:
            coord = []
            coor.append((ROW, COLUMN))
            COLUMN +=1
    ROW += 1
graph = np.array(maze)
coordinates = np.array(coor)

adjMatrixReg = np.array(calcAdjacencies.calcAdjacenciesRegular(graph, num_rows, num_columns))
adjMatrixDiag = np.array(calcAdjacenciesDiagnol.calcAdjacenciesDiagnol(graph, num_rows, num_columns))

visitedDFS = None
start = [0, 0, 1]
done = False

GRAPH = calcGRAPH.calcGRAPH(graph, coordinates, adjMatrixReg, adjMatrixDiag)
#for key in sorted(GRAPH.keys()) :
#    KEY = (key[0]+1, key[1]+1, key[2])
#    print(KEY , " : ", end = " (")
#    for item in GRAPH[key]:
#        print((item[0]+1, item[1]+1, item[2]), end=", ")
#    print(")\n")

path = []
dfs = DFS(GRAPH, start, visitedDFS, done, path)
