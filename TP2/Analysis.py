import time
import sys
import tp2 as algo
import tp2 as back
import math
import networkx as nx


#Set the recursion limit
sys.setrecursionlimit(100000)

#Create an objet to acces all algotithme methods
algo = algo.SortingAlgorithme()


'''
Dictionaries to call all files an analyse them
'''
nbNodeDictionary = {0: "10", 1: "14", 2: "18", 3: "22", 4: "26", 5: "30"}
graphWidthDictionary = {0: "4", 1: "6", 2: "8", 3: "10"}
versionDictionary = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h", 8: "i", 9: "j"}
time_dictionary = {"10": 0, "14": 0, "18": 0, "22": 0, "26": 0, "30": 0}
algoToDo = {0: "vorace", 1: "retourArriere", 2: "dynamique"}
avgArr = []
tempsmoy = 0

'''
All set of data in all files for all algorithme
'''
for n in range(1,2):
    for s in range(4,5):
        for m in range(0,1):
            print("tp2-donnees/poset" + str(nbNodeDictionary[s]) + "-" + str(graphWidthDictionary[m]))
            for i in range(4,5):
                timeArray = []
                avg = 0
                # Get the data in the file
                array = algo.fileToArray("tp2-donnees/poset" + str(nbNodeDictionary[s]) + "-" + str(graphWidthDictionary[m]) + str(versionDictionary[i]))

                if(algoToDo[n] == "vorace"):
                    G = nx.DiGraph()
                    G.add_edges_from(array)
                    t0 = time.time()
                    print(round(algo.voraceApproximation(G), 6))
                    t1 = time.time()
                    algoTime = t1 - t0
                    tempsmoy += algoTime

                if(algoToDo[n] == "retourArriere"):
                    graph = back.Graph(algo.nbNode)

                    #print(array)
                    for i in range(len(array)):
                        graph.addEdge(array[i][0], array[i][1])

                    t0 = time.time()
                    graph.topologicalSort()
                    t1 = time.time()
                    #print("count: " + str(graph.count))

                    algoTime = t1 - t0
                    tempsmoy += algoTime
                    print(graph.count)

            tempsmoy = tempsmoy/10
            print("Temps moyen: ")
            print(str(round(tempsmoy,6)))
            tempsmoy = 0