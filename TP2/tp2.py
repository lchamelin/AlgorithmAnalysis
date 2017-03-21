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

############################################################################
############################################################################


# instantiation dun algo de la class SortingAlgorithme
algo = SortingAlgorithme()
G = nx.DiGraph();

G.add_edges_from([(1, 0), (1, 4), (1, 8), (2, 5), (5, 8), (6, 0), (6, 2), (6, 4), (7, 2), (9, 3), (9, 6), (9, 7)])

print(G.number_of_nodes(), G.number_of_edges())

t = algo.transitive_reduction(G)

print(algo.voraceApproximation(G))






# Switch case qui permet de choisir le bon algo en fonctione des parametres
# passes au terminal par le user
'''
if(sys.argv[1] == "quick"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    array = algo.quickSort(array)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "quickRandom"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    array = algo.quickSortRandom(array)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "counting"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    array = algo.counting_sort(array, max(array))
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "quickSeuil"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    algo.quicksortSeuil(array, 0, len(array) - 1)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "quickRandomSeuil"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    algo.quicksortSeuilRandom(array, 0, len(array) - 1)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()


# calcul du temps pour l'execution de lalgo choisi.
algoTime = t1-t0

# Switch case pour gerer les options entrer au teminal
# Si un 'P' est entrer, les donnees seront imprime triees au terminal
# Si un 't' est entrer, le temps d'execution de tri sera imprime au terminal
if(len(sys.argv) >= 4):
    # Si 'p' est entre
    if(sys.argv[3] == "-p"):
        for elem in array:
            print(elem)
    # Si 't' est entre
    elif((sys.argv[3] == "-t")):
        print(algoTime)

    if(len(sys.argv) >= 5):
        # Si 'p' est entre
        if(sys.argv[4] == "-p"):
            for elem in array:
                print(elem)
        # Si 't' est entre
        elif((sys.argv[4] == "-t")):
            print(algoTime)

'''

