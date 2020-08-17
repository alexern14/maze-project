import calcTargets

def calcGRAPH(graph, coordinates, adjMatrixReg, adjMatrixDiag):
    GRAPH = {}
    for cell in coordinates:
        reg = True
        targetsVisited = []
        targets = []
        node = int(graph[cell[0], cell[1]])
        if node < 0:
            node = node * -1
        adjList = calcTargets.calcTARGETS(cell[0], cell[1], node, targetsVisited, targets, adjMatrixReg, adjMatrixDiag, reg, graph)
        CELL = [cell[0], cell[1], 1]
        if adjList is not None:
            GRAPH[tuple(CELL)] = tuple(adjList)
    for cell in coordinates:
        reg = False
        targetsVisited = []
        targets = []
        node = int(graph[cell[0], cell[1]])
        if node < 0:
            node = node * -1
        adjList = calcTargets.calcTARGETS(cell[0], cell[1], node, targetsVisited, targets, adjMatrixReg, adjMatrixDiag, reg, graph)
        CELL = [cell[0], cell[1], 0]
        if adjList is not None:
            GRAPH[tuple(CELL)] = tuple(adjList)
    return GRAPH

def calcGRAPHReg(graph, coordinates, adjMatrixReg, adjMatrixDiag):
    GRAPH = {}
    reg = True
    for cell in coordinates:
        targetsVisited = []
        targets = []
        node = int(graph[cell[0], cell[1]])
        if node < 0:
            node = node * -1
        adjList = calcTargets.calcTargets(cell[0], cell[1], node, targetsVisited, targets, reg, adjMatrixReg, adjMatrixDiag)
        if adjList is not None:
            GRAPH[tuple(cell)] = tuple(adjList)
    return GRAPH

def calcGRAPHDiag(graph, coordinates, adjMatrixReg, adjMatrixDiag):
    GRAPH = {}
    reg = False
    for cell in coordinates:
        targetsVisited = []
        targets = []
        node = int(graph[cell[0], cell[1]])
        if node < 0:
            node = node * -1
        adjList = calcTargets.calcTargets(cell[0], cell[1], node, targetsVisited, targets, reg, adjMatrixReg, adjMatrixDiag)
        if adjList is not None:
            GRAPH[tuple(cell)] = tuple(adjList)
    return GRAPH