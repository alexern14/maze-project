def checkPathLenth(thisRow, thisColumn, targetsVisited, pathlength, graph, targets, reg, adj, row, column, adjMatrixReg, adjMatrixDiag, bool):
    if [thisRow, thisColumn] not in targetsVisited:
        targetsVisited.append([thisRow, thisColumn])
        if pathlength == 0:
            return
        if pathlength == 1:
            node = int(graph[adj[0], adj[1]])
            if node < 0:
                if reg:
                    bool = 0
                else:
                    bool = 1
            if [thisRow, thisColumn] not in targets:
                targets.append([thisRow, thisColumn, bool])
        else:
            calcTARGETSsHelper(row, column, thisRow, thisColumn, pathlength - 1, targetsVisited, targets,
                               reg,
                               adjMatrixReg, adjMatrixDiag, graph)
        targetsVisited.remove([thisRow, thisColumn])

def calcTARGETSsHelper(oldRow, oldColumn, row, column, pathlength, targetsVisited, targets, reg, adjMatrixReg, adjMatrixDiag, graph):
    if reg:
        bool = 1
        adjLists = adjMatrixReg[row][column]
        for adj in adjLists:
            thisRow = adj[0]
            thisColumn = adj[1]
            if oldRow == row == thisRow:
                checkPathLenth(thisRow, thisColumn, targetsVisited, pathlength, graph, targets, reg, adj, row, column,
                               adjMatrixReg, adjMatrixDiag, bool)
            elif oldColumn == column ==thisColumn:
                checkPathLenth(thisRow, thisColumn, targetsVisited, pathlength, graph, targets, reg, adj, row, column,
                               adjMatrixReg, adjMatrixDiag, bool)
        return targets
    else:
        bool = 0
        adjLists = adjMatrixDiag[row][column]
        for adj in adjLists:
            thisRow = adj[0]
            thisColumn = adj[1]
            if oldRow+2 == row+1 == thisRow:
                if oldColumn+2 == column+1 == thisColumn:
                    checkPathLenth(thisRow, thisColumn, targetsVisited, pathlength, graph, targets, reg, adj, row,
                                   column, adjMatrixReg, adjMatrixDiag, bool)
            if oldRow+2 == row+1 == thisRow:
                if oldColumn-2 == column-1 == thisColumn:
                    checkPathLenth(thisRow, thisColumn, targetsVisited, pathlength, graph, targets, reg, adj, row,
                                   column, adjMatrixReg, adjMatrixDiag, bool)
            if oldRow-2 == row-1 == thisRow:
                if oldColumn-2 == column-1 == thisColumn:
                    checkPathLenth(thisRow, thisColumn, targetsVisited, pathlength, graph, targets, reg, adj, row,
                                   column, adjMatrixReg, adjMatrixDiag, bool)
            if oldRow-2 == row-1 == thisRow:
                if oldColumn+2 == column+1 == thisColumn:
                    checkPathLenth(thisRow, thisColumn, targetsVisited, pathlength, graph, targets, reg, adj, row,
                                   column, adjMatrixReg, adjMatrixDiag, bool)

def calcTARGETS(row, column, pathLength, targetsVisited, targets, adjMatrixReg, adjMatrixDiag, reg, graph):
    if reg:
        adjLists = adjMatrixReg[row][column]
        bool = 1
    else:
        adjLists = adjMatrixDiag[row][column]
        bool = 0
    if [row, column] not in targetsVisited:
        targetsVisited.append([row, column])
    for adj in adjLists:
        thisRow = adj[0]
        thisColumn = adj[1]
        if [thisRow, thisColumn] not in targetsVisited:
            targetsVisited.append([thisRow, thisColumn])
            if pathLength == 0:
                return
            if pathLength == 1:
                node = int(graph[adj[0], adj[1]])
                if node < 0:
                    if reg:
                        bool = 0
                    else:
                        bool = 1
                if [thisRow, thisColumn, bool] not in targets:
                    targets.append([thisRow, thisColumn, bool])
            else:
                calcTARGETSsHelper(row, column, thisRow, thisColumn, pathLength - 1, targetsVisited, targets, reg, adjMatrixReg, adjMatrixDiag, graph)
            targetsVisited.remove([thisRow, thisColumn])
    return targets




def calcTargetsHelper(oldRow, oldColumn, row, column, pathlength, targetsVisited, targets, reg, adjMatrixReg, adjMatrixDiag):
    if reg:
        adjLists = adjMatrixReg[row][column]
        for adj in adjLists:
            thisRow = adj[0]
            thisColumn = adj[1]
            if oldRow == row == thisRow:
                if [thisRow, thisColumn] not in targetsVisited:
                    targetsVisited.append([thisRow, thisColumn])
                    if pathlength == 0:
                        return
                    if pathlength == 1:
                        if [thisRow, thisColumn] not in targets:
                            targets.append([thisRow, thisColumn])
                    else:
                        calcTargetsHelper(row, column, thisRow, thisColumn, pathlength - 1, targetsVisited, targets,
                                          reg,
                                          adjMatrixReg, adjMatrixDiag)
                    targetsVisited.remove([thisRow, thisColumn])
            elif oldColumn == column ==thisColumn:
                if [thisRow, thisColumn] not in targetsVisited:
                    targetsVisited.append([thisRow, thisColumn])
                    if pathlength == 0:
                        return
                    if pathlength == 1:
                        if [thisRow, thisColumn] not in targets:
                            targets.append([thisRow, thisColumn])
                    else:
                        calcTargetsHelper(row, column, thisRow, thisColumn, pathlength - 1, targetsVisited, targets,
                                          reg,
                                          adjMatrixReg, adjMatrixDiag)
                    targetsVisited.remove([thisRow, thisColumn])
        return targets
    else:
        adjLists = adjMatrixDiag[row][column]
        for adj in adjLists:
            thisRow = adj[0]
            thisColumn = adj[1]
            if oldRow+2 == row+1 == thisRow:
                if oldColumn+2 == column+1 == thisColumn:
                    if [thisRow, thisColumn] not in targetsVisited:
                        targetsVisited.append([thisRow, thisColumn])
                        if pathlength == 0:
                            return
                        if pathlength == 1:
                            if [thisRow, thisColumn] not in targets:
                                targets.append([thisRow, thisColumn])
                        else:
                            calcTargetsHelper(row, column, thisRow, thisColumn, pathlength - 1, targetsVisited, targets,
                                              reg,
                                              adjMatrixReg, adjMatrixDiag)
                        targetsVisited.remove([thisRow, thisColumn])
            if oldRow+2 == row+1 == thisRow:
                if oldColumn-2 == column-1 == thisColumn:
                    if [thisRow, thisColumn] not in targetsVisited:
                        targetsVisited.append([thisRow, thisColumn])
                        if pathlength == 0:
                            return
                        if pathlength == 1:
                            if [thisRow, thisColumn] not in targets:
                                targets.append([thisRow, thisColumn])
                        else:
                            calcTargetsHelper(row, column, thisRow, thisColumn, pathlength - 1, targetsVisited, targets,
                                              reg,
                                              adjMatrixReg, adjMatrixDiag)
                        targetsVisited.remove([thisRow, thisColumn])
            if oldRow-2 == row-1 == thisRow:
                if oldColumn-2 == column-1 == thisColumn:
                    if [thisRow, thisColumn] not in targetsVisited:
                        targetsVisited.append([thisRow, thisColumn])
                        if pathlength == 0:
                            return
                        if pathlength == 1:
                            if [thisRow, thisColumn] not in targets:
                                targets.append([thisRow, thisColumn])
                        else:
                            calcTargetsHelper(row, column, thisRow, thisColumn, pathlength - 1, targetsVisited, targets,
                                              reg,
                                              adjMatrixReg, adjMatrixDiag)
                        targetsVisited.remove([thisRow, thisColumn])
            if oldRow-2 == row-1 == thisRow:
                if oldColumn+2 == column+1 == thisColumn:
                    if [thisRow, thisColumn] not in targetsVisited:
                        targetsVisited.append([thisRow, thisColumn])
                        if pathlength == 0:
                            return
                        if pathlength == 1:
                            if [thisRow, thisColumn] not in targets:
                                targets.append([thisRow, thisColumn])
                        else:
                            calcTargetsHelper(row, column, thisRow, thisColumn, pathlength - 1, targetsVisited, targets,
                                              reg,
                                              adjMatrixReg, adjMatrixDiag)
                        targetsVisited.remove([thisRow, thisColumn])



def calcTargets(row, column, pathLength, targetsVisited, targets, reg, adjMatrixReg, adjMatrixDiag):
    if reg:
        adjLists = adjMatrixReg[row][column]
    else:
        adjLists = adjMatrixDiag[row][column]
    if [row, column] not in targetsVisited:
        targetsVisited.append([row, column])
    for adj in adjLists:
        thisRow = adj[0]
        thisColumn = adj[1]
        if [thisRow, thisColumn] not in targetsVisited:
            targetsVisited.append([thisRow, thisColumn])
            if pathLength == 0:
                return
            if pathLength == 1:
                if [thisRow, thisColumn] not in targets:
                    targets.append([thisRow, thisColumn])
            else:
                calcTargetsHelper(row, column, thisRow, thisColumn, pathLength - 1, targetsVisited, targets, reg, adjMatrixReg, adjMatrixDiag)
            targetsVisited.remove([thisRow, thisColumn])
    return targets