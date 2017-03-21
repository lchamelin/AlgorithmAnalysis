import os
import random
import time
import matplotlib.pyplot as plt
import sys
import tp2 as algo
import math
import numpy as np
import networkx as nx

#Set the recursion limit
sys.setrecursionlimit(100000)

#Create an objet to acces all algotithme methods
algo = algo.SortingAlgorithme()


'''
Dictionaries to call all files an analyse them
'''
nbNodeDictionary = {0: "10", 1: "14", 2: "18", 3: "22", 4: "26", 5: "30"}
graphWidthDictionary = {0: "4", 1: "6", 2: "8"}
versionDictionary = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}
time_dictionary = {"10": 0, "14": 0, "18": 0, "22": 0, "26": 0, "30": 0}
algoToDo = {0: "vorace", 1: "dynamique", 2: "retourArriere"}
avgArr = []

'''
All set of data in all files for all algorithme
'''

for s in range(0,6):
    for m in range(0,3):
        for i in range(0,10):
            timeArray = []
            avg = 0
            # Get the data in the file
            array = algo.fileToArray("tp2-donnees/poset" + str(nbNodeDictionary[s]) + "-" + str(graphWidthDictionary[m]) + str(versionDictionary[i]))
            t0 = time.time()
            G = nx.DiGraph()
            G.add_edges_from(array)

            #Print the number of nodfes and edges
            #print(G.number_of_nodes(), G.number_of_edges())
            t = algo.transitive_reduction(G)
            t1 = time.time()
            algoTime = t1 - t0

            print(str(nbNodeDictionary[s]) + "-" + str(graphWidthDictionary[m]) + str(versionDictionary[i]) + ": " + str(algo.voraceApproximation(G)))
            #print("Time: " + str(algoTime))
