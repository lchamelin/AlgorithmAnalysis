import os
import random
import time
import sys
import math



############################################################################
#TESTING THE METHODS
############################################################################


############################################################################
#IF ELSE to chose the right algorithm from the terminal
############################################################################
'''
algo = SortingAlgorithme()
if(sys.argv[1] == "vorace"):
    G = nx.DiGraph()
    array = algo.fileToArray("tp2-donnees/poset" + str(sys.argv[2]))
    G.add_edges_from(array)
    #Start timer
    t0 = time.time()
    nbExtentionLineaire = round(algo.voraceApproximation(G), 6)
    #Get the execution time of the algorithme
    t1 = time.time()
elif (sys.argv[1] == "retourArriere"):
    array = algo.fileToArray("tp2-donnees/poset" + str(sys.argv[2]))
    #Start timer
    t0 = time.time()
    graph = Graph(algo.nbNode)
    # Append all edges to the graph
    for i in range(len(array)):
        graph.addEdge(array[i][0], array[i][1])

    graph.topologicalSort()
    # Get the number of linear expression from the graphe
    nbExtentionLineaire = graph.count
    #Get the execution time of the algorithme
    t1 = time.time()

elif (sys.argv[1] == "dynamique"):
    array = algo.fileToArray("tp2-donnees/poset" + str(sys.argv[2]))
    #Start timer
    t0 = time.time()
    print("Algorithm non fonctionnel presentement pour le fichier -> " + "tp2-donnees/poset" + str(sys.argv[2]))
    nbExtentionLineaire = 0
    #Get the execution time of the algorithme
    t1 = time.time()


#Calculate time for the algorithm execution
algoTime = t1-t0
#IF ELSE to execute the 3 different algorithm
#If P is entered, we print the number on linear extension to the terminal
#If t is entered, we print the execution time to the terminal
if(len(sys.argv) >= 4):
    # Si 'p' est entre
    if(sys.argv[3] == "-p"):
        print("Nombre d'extensions lineaires: " + str(nbExtentionLineaire))
    # Si 't' est entre
    elif((sys.argv[3] == "-t")):
        print("Temps d'execution pour l'algo choisi: " + str(algoTime) + " secondes")
    if(len(sys.argv) >= 5):
        # Si 'p' est entre
        if(sys.argv[4] == "-p"):
            print("Nombre d'extensions lineaires: " + str(nbExtentionLineaire))
        # Si 't' est entre
        elif((sys.argv[4] == "-t")):
            print("Temps d'execution pour l'algo choisi: " + str(algoTime) + " secondes")
'''