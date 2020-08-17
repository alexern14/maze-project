import numpy as np
import calcAdjacencies
import calcAdjacenciesDiagnol
import calcGRAPH

def backtrace(parent, start, end):
    path = []
    path.append(end)
    while path[-1] != start:
        next = [parent[tuple(path[-1])][0], parent[tuple(path[-1])][1]]
        path.append(next)
    path.reverse()
    for position in path:
        position[0] +=1
        position[1] +=1
    return path

def BFS(graphReg, graphDiag):
    regular = True
    parent = {}
    tempPath = 0
    while queue:
        node = queue.pop(0)
        if node != [0, 0]:
            tempPath = []
            tempPath.append(node)
            parentNode = [parent.get(tuple(node))[0], parent.get(tuple(node))[1]]
            tempPath.append(parentNode)
            count = 0
            tempNode = 0
            while parent.get(tuple(parentNode)) and count != 1:
                parentNode = [parent.get(tuple(parentNode))[0], parent.get(tuple(parentNode))[1]]
                if parentNode == tempNode:
                    count = 1
                tempNode = parentNode
                tempPath.append(parentNode)
        nodeInt = graph[node[0], node[1]]
        if node == [7, 7]:
           return backtrace(parent, [0, 0], [7, 7])
        if tempPath != 0:
            regular = True
            tempPath.reverse()
            for node in tempPath:
                if graph[node[0], node[1]] < 0:
                    if regular == True:
                        regular = False
                    else:
                        regular = True
        if regular:
            for NODE in graphReg[tuple(node)]:
                if visited[NODE[0], NODE[1]] == False:
                    queue.append(NODE)
                    visited[NODE[0], NODE[1]] = True
                    parent[tuple(NODE)] = tuple(node)
        else:
            for NODE in graphDiag[tuple(node)]:
                if visited[NODE[0], NODE[1]] == False:
                    queue.append(NODE)
                    visited[NODE[0], NODE[1]] = True
                    parent[tuple(NODE)] = tuple(node)

def dfs(graphReg, graphDiag, start, visited, prev):
    if visited is None:
        visited = []
    if start in visited:
        return
    visited.append(start)
    if start == [7, 7]:
        return visited
    regular = True
    for node in visited:
        if graph[node[0], node[1]] < 0:
            if regular == True:
                regular = False
            else:
                regular = True
    if regular:
        NEXT = graphReg[tuple(start)]
    else:
        NEXT = graphDiag[tuple(start)]
    for next in NEXT:
        dfs(graphReg, graphDiag, next, visited, prev)
    visited.pop()
    return visited

def DFS(graph, start, visited, done):
    if visited is None:
        visited = []
    if start in visited:
        return
    #if start[2] == 0:
    #    if start in visited:
    #        return
    #    if [start[0], start[1], 1] in visited:
    #        return
    #if start[2] == 1:
    #    if start in visited:
    #        return
    #    if [start[0], start[1], 0] in visited:
    #        return
    visited.append(start)
    if start == [7, 7, 1]:
        done = True
        return visited
    if start == [7, 7, 0]:
        done = True
        return visited
    NEXT = graph[tuple(start)]
    for next in NEXT:
        DFS(graph, next, visited, done)
    if done != True:
        visited.pop()
    return visited

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

visited = [False] * (graph)
visited[0][0] = True
queue = []
queue.append([0, 0])

visitedDFS = None
start = [0, 0, 1]
done = False

GRAPH = calcGRAPH.calcGRAPH(graph, coordinates, adjMatrixReg, adjMatrixDiag)
#for key in sorted(GRAPH.keys()) :
#    KEY = (key[0]+1, key[1]+1, key[2])
#    print(KEY , " : ", end = " (")
#    for item in GRAPH[key]:
#        print((item[0]+1, item[1]+1), item[2], end=", ")
#    print(")\n")

#GRAPHreg = calcGRAPH.calcGRAPHReg(graph, coordinates, adjMatrixReg, adjMatrixDiag)
#GRAPHdiag = calcGRAPH.calcGRAPHDiag(graph, coordinates, adjMatrixReg, adjMatrixDiag)
#for key in sorted(GRAPHreg.keys()) :
#    KEY = (key[0]+1, key[1]+1)
#    print(KEY , " : ", end = " (")
#    for item in GRAPHreg[key]:
#        print((item[0]+1, item[1]+1), end=", ")
#    print(")\n")
#for key in sorted(GRAPHdiag.keys()) :
#    KEY = (key[0] + 1, key[1] + 1)
#    print(KEY, " : ", end=" (")
#    for item in GRAPHdiag[key]:
#        print((item[0] + 1, item[1] + 1), end=", ")
#    print(")\n")

dfs = DFS(GRAPH, start, visitedDFS, done)
print(dfs)

#DFS = dfs(GRAPHreg, GRAPHdiag, start, visitedDFS, prev=None)
#print(DFS)

#PATH = BFS(GRAPHreg, GRAPHdiag)
#print(PATH)