import scripts.logic.dijkstra as dijkstra
import scripts.logic.graphs as graphs

import scripts.logic.bigM as bigM

import scripts.interface.console.screen as screen

def dijkstraOptions():
    
    print("             PARÁMETROS\n")
    nodes = int(input("Indica el número total de nodos: "))
    screen.clearConsole()

    matrixNodes = []

    for i in range(nodes):

        distanceNodes = []
        for j in range(nodes):

            init = ord("A") + i
            destiny = ord("A") + j

            if i != j:
                distance = int(input("Ingrese la distancia del nodo " + chr(init)
                                    + " al nodo " + chr(destiny) + ": "))
            else: distance = 0

            distanceNodes.append(distance)
            screen.clearConsole()
        
        matrixNodes.append(distanceNodes)

    """matrixNodes = [[0, 2, 0, 0, 0, 1, 0, 0],
                   [2, 0, 2, 2, 4, 0, 0, 0],
                   [0, 2, 0, 0, 3, 0, 0, 1],
                   [0, 2, 0, 0, 4, 3, 0, 0],
                   [0, 4, 3, 4, 0, 0, 7, 0],
                   [1, 0, 0, 3, 0, 0, 5, 0],
                   [0, 0, 0, 0, 7, 5, 0, 6],
                   [0, 0, 1, 0, 0, 0, 6, 0]]
    """

    init = input("Indica el nodo inicial: ")
    destiny = input("Indica el nodo destino: ")

    screen.clearConsole()

    initNode = ord(init.upper()) - ord("A")
    destinyNode = ord(destiny.upper()) - ord("A")

    result = dijkstra.find_shortest_path(matrixNodes, initNode, destinyNode)
    asciiResult = [chr(65 + node) for node in result]
    stringResult = ""
    for i in range(len(asciiResult)):
        if i != len(asciiResult)-1:
            stringResult += asciiResult[i] + "->"
        else: stringResult += asciiResult[i]

    print("El camino más corto es: " + stringResult)

    distance = dijkstra.find_shortest_distance(matrixNodes,initNode, destinyNode)
    print("La distancia más corta es: " + str(distance))

    showGraph = input("¿Deseas mostrar la red? [Y/N]: ").upper()
    if showGraph == "Y": graphs.undirected_graph(matrixNodes, "prueba")

def bigMOptions():
    print('\nEjemplo 1\n---------')
    f = 0

    c = [5, 4]
    A = [[2, 1], [1, 1],[1, 2]]
    b = [20, 18, 12]
    inq = [-1, -1, 1]
    bigM.simplex(A,b,c,inq,'max',f)