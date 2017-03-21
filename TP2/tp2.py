import os
import random
import time
import sys
import math
import numpy as np
import networkx as nx


class SortingAlgorithme:
    def enumerate_dag(self, g):
      def enumerate_r(n, paths, visited, a_path = []):
        a_path += [n]
        visited[n] = 1
        if not g[n]:
            paths += [list(a_path)]
        else:
            for nn in g[n]:
                enumerate_r(nn, paths, visited, list(a_path))

      paths, N = [], len(g)
      visited = np.zeros((N), dtype='int32')

      for root in range(N):
        if visited[root]: continue
        enumerate_r(root, paths, visited, [])

      return paths


    def transitive_reduction(self, G):
        """
        References:
        https://en.wikipedia.org/wiki/Transitive_reduction
        """
        TR = nx.DiGraph()
        TR.add_nodes_from(G.nodes())
        for u in G:
            u_edges = set(G[u])
            for v in G[u]:
                u_edges -= {y for x, y in nx.dfs_edges(G, v)}
            TR.add_edges_from((u,v) for v in u_edges)
        return TR


    #Get the longest path
    def dag_longest_path(self, G, weight='weight', default_weight=1):
        if(G.number_of_edges() !=0):
            dist = {}
            for v in nx.topological_sort(G):
                us = [(dist[u][0] + data.get(weight, default_weight), u)
                    for u, data in G.pred[v].items()]
                # Use the best predecessor if there is one and its distance is non-negative, otherwise terminate.
                maxu = max(us, key=lambda x: x[0]) if us else (0, v)
                dist[v] = maxu if maxu[0] >= 0 else (0, v)
            u = None
            v = max(dist, key=lambda x: dist[x][0])
            path = []
            while u != v:
                path.append(v)
                u = v
                v = dist[v][1]
            path.reverse()
            return path


    #Calculate all chains
    def calculateAllChains(self, G):
        algo = SortingAlgorithme()
        L = []
        c = []
        c = algo.dag_longest_path(G)

        # Get nodes that have edges with other nodes
        while G.number_of_edges() != 0:
            G.remove_nodes_from(c)
            L.append(c)
            c = algo.dag_longest_path(G)

        #Append the node that have no more edges
        for i in G.nodes():
            L.append([i])

        return L


    # Algorithme 1 (Vorace)
    def voraceApproximation(self, G):
        algo = SortingAlgorithme()
        nbNode = G.number_of_nodes()

        longestChains = algo.calculateAllChains(G)
        nbExtensionLineaire = len(longestChains)

        h = 0
        for i in range (1, nbExtensionLineaire):
            h += -(len(longestChains[i]) / G.number_of_nodes()) * (math.log(len(longestChains[i]) / G.number_of_nodes(), 2))

        expo = (0.5 * nbNode * h)
        nbExtensionLineaireApprox = math.pow(2, expo)

        return nbExtensionLineaireApprox


    #Append to an array what we read from the file
    def fileToArray(self, file):
        with open(file, "r") as f:
            #Array to
            array = []
            #To skip the first line
            next(f)

            for line in f:
                int_list = [int(i) for i in line.split()]
                array.append(int_list)
                #print(int_list)

            return array


############################################################################
############################################################################

# instantiation dun algo de la class SortingAlgorithme
algo = SortingAlgorithme()
G = nx.DiGraph();

array = algo.fileToArray("tp2-donnees/poset10-4c")
G.add_edges_from(array)

print(G.number_of_nodes(), G.number_of_edges())

transitiveGraph = algo.transitive_reduction(G)

print(algo.voraceApproximation(transitiveGraph))

# Switch case qui permet de choisir le bon algo en fonctione des parametres
# passes au terminal par le user
'''
if(sys.argv[1] == "vorace"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    G.add_edges_from(theArray)
    t = algo.transitive_reduction(G)
    nbExtentionLineaire = algo.voraceApproximation(G)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "dynamique"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    array = algo.quickSortRandom(array)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "retourArriere"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    array = algo.counting_sort(array, max(array))
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()


#Calculate time for the algorithm execution
algoTime = t1-t0

#IF ELSE to execute the 3 different algorithm
#If P is entered, we print the number on linear extension to the terminal
#If t is entered, we print the execution time to the terminal
if(len(sys.argv) >= 4):
    # Si 'p' est entre
    if(sys.argv[3] == "-p"):
        print(nbExtentionLineaire)
    # Si 't' est entre
    elif((sys.argv[3] == "-t")):
        print(algoTime)

    if(len(sys.argv) >= 5):
        # Si 'p' est entre
        if(sys.argv[4] == "-p"):
            print(nbExtentionLineaire)
        # Si 't' est entre
        elif((sys.argv[4] == "-t")):
            print(algoTime)

'''