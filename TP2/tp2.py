import os
import random
import time
import sys
import math
import numpy as np
import networkx as nx
# Python program to print topological sorting of a DAG
from collections import defaultdict

# Class to represent a graph
class Graph:
    """
    References:
    http: // www.geeksforgeeks.org / all - topological - sorts - of - a - directed - acyclic - graph /
    """

    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.count = 0
        self.visited = []
        self.indegree = []

        #Initialising all indegree with 0
        for i in range(0, self.V):
            self.indegree.append(0)
        #print(self.indegree)

    #function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.indegree[v] += 1

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, stack, visited):
        #Know if we all found the topological sort
        flag = False

        for i in range(self.V):

            if (self.indegree[i] == 0 and self.visited[i] == False):
                for j in range(len(self.graph[i])):
                    self.indegree[self.graph[i][j]] -= 1

                stack.append(i)
                self.visited[i] = True
                self.topologicalSortUtil(stack, visited)

                self.visited[i] = False
                stack.pop()

                for j in range(len(self.graph[i])):
                    self.indegree[self.graph[i][j]] += 1

                flag = True

        if(flag == False):
            self.count += 1
            print(self.count)


    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        print(self.V)

        for i in range(0, self.V):
            self.visited.append(False)
        stack = []
        #print(self.visited)

        self.topologicalSortUtil(stack, self.visited)

class SortingAlgorithme:
    """
    References:
    https: // networkx.github.io / documentation / networkx - 1.10 / tutorial / tutorial.html
    """
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
            print(path)
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
        print(L)
        return L


    # Algorithme 1 (Vorace)
    def voraceApproximation(self, G):
        algo = SortingAlgorithme()
        nbNode = G.number_of_nodes()
        print(nbNode)

        longestChains = algo.calculateAllChains(G)
        nbExtensionLineaire = len(longestChains)

        h = 0
        for i in range (1, nbExtensionLineaire):
            h += -(len(longestChains[i]) / nbNode) * (math.log(len(longestChains[i]) / nbNode, 2))

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

array = algo.fileToArray("tp2-donnees/poset10-4a")
G.add_edges_from(array)

#print(G.number_of_nodes(), G.number_of_edges())

transitiveGraph = algo.transitive_reduction(G)


print(algo.voraceApproximation(transitiveGraph))

#graph = Graph(G.number_of_nodes())
#print(array)

#for i in range(len(array)):
    #graph.addEdge(array[i][0], array[i][1])

"""
graph.addEdge(1,0)
graph.addEdge(1, 4)
graph.addEdge(1, 8)
graph.addEdge(2, 5)
graph.addEdge(5, 8)
graph.addEdge(6, 0)
graph.addEdge(6, 2)
graph.addEdge(6, 4)
graph.addEdge(7, 2)
graph.addEdge(9, 3)
graph.addEdge(9, 6)
graph.addEdge(9, 7)
"""


#graph.topologicalSort()


#print(graph.count)

# IF ELSE to chose the right algorithm from the terminal
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