from graphviz import Graph


def undirected_graph(matrix, name="weighted_undirected_graph"):

    n = len(matrix)
    f = Graph(name, filename="Graphs//"+name+'.gv')
    f.attr('node', shape='circle')
    for i in range(n):
        f.node(chr(ord("A")+i))

    for i in range(n):
        for j in range(n):
            if matrix[i][j] != 0 and i < j:
                f.edge(chr(ord("A")+i), chr(ord("A")+j), label=str(matrix[i][j]))

    return f.view()