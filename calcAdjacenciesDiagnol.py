def calcAdjacenciesDiagnol(graph, num_rows, num_columns):
    adjMatrix = []
    for i in range(0, num_rows):
        adjListRow = []
        for j in range(0, num_columns):
            adjList = []
            if (i - 1) >= 0:
                if (j - 1) >= 0:
                    adj = [i-1, j-1]
                    adjList.append(adj)
            if (i + 1) < num_rows:
                if (j + 1) < num_columns:
                    adj = [i + 1, j+1]
                    adjList.append(adj)
            if (j - 1) >= 0:
                if (i + 1) < num_rows:
                    adj = [i+1, j - 1]
                    adjList.append(adj)
            if (j + 1) < num_columns:
                if (i - 1) >= 0:
                    adj = [i-1, j + 1]
                    adjList.append(adj)
            adjListRow.append(adjList)
        adjMatrix.append(adjListRow)
    return adjMatrix