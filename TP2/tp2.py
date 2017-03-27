import os
import random
import time
import sys
import math
import numpy
import networkx as nx
# Python program to print topological sorting of a DAG
from collections import defaultdict

# Class to represent a graph
class Graph:
    #References:
    #http: // www.geeksforgeeks.org / all - topological - sorts - of - a - directed - acyclic - graph /
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices
        self.count = 0
        self.visited = []
        self.indegree = []
        self.nbNode = 0

        #Initialising all indegree with 0
        for i in range(self.V):
            self.indegree.append(0)

    #function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
        #print(v)
        #print(self.indegree)
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


    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        for i in range(self.V):
            self.visited.append(False)
        stack = []

        self.topologicalSortUtil(stack, self.visited)


    # # A utility function to print the solution
    # def printSolution(self, reach):
    #     print ("Following matrix transitive closure of the given graph ")
    #     for i in range(self.V):
    #         for j in range(self.V):
    #             print "%7d\t" % (reach[i][j]),
    #         print ""
    #
    # # Prints transitive closure of graph[][] using Floyd Warshall algorithm
    # def transitiveClosure(self, graph):
    #     '''reach[][] will be the output matrix that will finally
    #     have reachability values.
    #     Initialize the solution matrix same as input graph matrix'''
    #     reach = [i[:] for i in graph]
    #     '''Add all vertices one by one to the set of intermediate
    #     vertices.
    #     ---> Before start of a iteration, we have reachability value
    #     for all pairs of vertices such that the reachability values
    #      consider only the vertices in set
    #     {0, 1, 2, .. k-1} as intermediate vertices.
    #     ----> After the end of an iteration, vertex no. k is
    #     added to the set of intermediate vertices and the
    #     set becomes {0, 1, 2, .. k}'''
    #     for k in range(self.V):
    #
    #         # Pick all vertices as source one by one
    #         for i in range(self.V):
    #
    #             # Pick all vertices as destination for the
    #             # above picked source
    #             for j in range(self.V):
    #                 # If vertex k is on a path from i to j,
    #                 # then make sure that the value of reach[i][j] is 1
    #                 reach[i][j] = reach[i][j] or (reach[i][k] and reach[k][j])
    #
    #     self.printSolution(reach)

class SortingAlgorithme:
    #References:
    #https: // networkx.github.io / documentation / networkx - 1.10 / tutorial / tutorial.html
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
      visited = numpy.zeros((N), dtype='int32')

      for root in range(N):
        if visited[root]: continue
        enumerate_r(root, paths, visited, [])

      return paths


    def transitive_reduction(self, G):
        #References:
        #https://en.wikipedia.org/wiki/Transitive_reduction
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
            #print(path)
            return path


    #Calculate all chains
    def calculateAllChains(self, G):
        algo = SortingAlgorithme()
        L = []
        c = []
        c = algo.dag_longest_path(G)

        #Get nodes that have edges with other nodes
        while G.number_of_edges() != 0:
            G.remove_nodes_from(c)
            L.append(c)
            c = algo.dag_longest_path(G)

        #Append the node that have no more edges
        for i in G.nodes():
            L.append([i])
        #print(L)
        return L


    def voraceApproximation(self, G):
        algo = SortingAlgorithme()
        nbNode = self.nbNode
        #print("Nb nodes: " + str(nbNode))

        longestChains = algo.calculateAllChains(G)
        nbChains = len(longestChains)
        #print(nbChains)

        h = 0
        for i in range (0, nbChains):
            h += -(len(longestChains[i]) / nbNode) * (math.log(len(longestChains[i]) / nbNode, 2))

        expo = (0.5 * nbNode * h)
        nbExtensionLineaireApprox = math.pow(2, expo)

        return nbExtensionLineaireApprox


    # Append to an array what we read from the file
    def fileToArray(self, file):
        with open(file, "r") as f:
            array = []
            # To get the num ber of nodes
            self.nbNode = int(f.readline()[0: 2])

            for line in f:
                int_list = [int(i) for i in line.split()]
                array.append(int_list)
                # print(int_list)

            return array


############################################################################
#TESTING THE METHODS
############################################################################

#Instantiation of an objet to get all function for the vorace algorithme


#Get all line of text file to an array
# array = algo.fileToArray("tp2-donnees/poset10-4a")
#print(array)

#Create a graphe from the library we use: networkx



#Get the longest chain
#longestChains = algo.calculateAllChains(G)

#Apply the vorace approximation
# graph.printSolution(graph.graph)
# graph.transitiveClosure(graph)
# print(round(algo.voraceApproximation(G), 6))

#
# #Instantiation of an object to get all function of the backtracking algorithme
# graph = Graph(algo.nbNode)
#
# #Append all edges to the graph
# for i in range(len(array)):
#     graph.addEdge(array[i][0], array[i][1])
#
# graph.topologicalSort()
#
# #Get the number of linear expression from the graphe
# print("count: " + str(graph.count))

############################################################################
#IF ELSE to chose the right algorithm from the terminal
############################################################################
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