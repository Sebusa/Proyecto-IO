from math import inf

def find_all(nodesMatrix, start, end):    
    n = len(nodesMatrix)

    dist = [inf]*n
    dist[start] = nodesMatrix[start][start]  # 0

    spVertex = [False]*n
    parent = [-1]*n

    path = [{}]*n

    for count in range(n-1):
        minix = inf
        u = 0

        for v in range(len(spVertex)):
            if spVertex[v] == False and dist[v] <= minix:
                minix = dist[v]
                u = v

        spVertex[u] = True
        for v in range(n):
            if not(spVertex[v]) and nodesMatrix[u][v] != 0 and dist[u] + nodesMatrix[u][v] < dist[v]:
                parent[v] = u
                dist[v] = dist[u] + nodesMatrix[u][v]

    for i in range(n):
        j = i
        s = []
        while parent[j] != -1:
            s.append(j)
            j = parent[j]
        s.append(start)
        path[i] = s[::-1]

    return (dist[end], path[end]) if end >= 0 else (dist, path)


def find_shortest_path(nodesMatrix, start, end):
    return find_all(nodesMatrix, start, end)[1]


def find_shortest_distance(nodesMatrix, start, end):
    return find_all(nodesMatrix, start, end)[0]