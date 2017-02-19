import os
import random
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import sys
import Tp1 as algo
import math


sys.setrecursionlimit(100000)
algo = algo.SortingAlgorithme()


'''
Dictionaries to call all files in all folder
'''

data_dictionary = {0: "1000", 1: "5000", 2: "10000", 3: "50000", 4: "100000", 5: "500000"}
time_dictionary = {"1000" : 0, "5000" : 0, "10000" : 0, "50000" : 0, "100000" : 0, "500000" : 0}
folder_data = {0: "0_9", 1: "10_19", 2: "20_29"}
algoToDo = {0: "counting", 1: "quickSort", 2: "quickSortRandom", 3: "quickSortSeuil", 4: "quickSortSeuilRandom"}
avgArr = []
taille = [1000, 5000, 10000, 50000, 100000, 500000]

'''
All set of data in all folder for all algorithme
'''
for s in range(4,5):
    for m in range(0,3):
        print("Folder " + folder_data[m] + ":")
        avgArr = []
        for i in range(0,6):
            timeArray = []
            avg = 0

            if folder_data[m] == "0_9":
                for j in range(1,10):
                    array = algo.fileToArray(folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt")

                    if (algoToDo[s] == "counting"):
                        t0 = time.time()
                        a = algo.counting_sort(array, max(array))
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if(algoToDo[s] == "quickSort"):
                        t0 = time.time()
                        a = algo.quickSort(array)
                        t1 = time.time()
                        algoTime = t1-t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortRandom"):
                        t0 = time.time()
                        a = algo.quickSortRandom(array)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortSeuil"):
                        t0 = time.time()
                        algo.quicksortSeuil(array, 0, len(array) - 1)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortSeuilRandom"):
                        t0 = time.time()
                        algo.quicksortSeuilRandom(array, 0, len(array) - 1)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    #Append sorting time to an array
                    timeArray.append(algoTime)


            if folder_data[m] == "10_19":
                for j in range(10,20):
                    array = algo.fileToArray(folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt")
                    if (algoToDo[s] == "counting"):
                        t0 = time.time()
                        a = algo.counting_sort(array, max(array))
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if(algoToDo[s] == "quickSort"):
                        t0 = time.time()
                        a = algo.quickSort(array)
                        t1 = time.time()
                        algoTime = t1-t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortRandom"):
                        t0 = time.time()
                        a = algo.quickSortRandom(array)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortSeuil"):
                        t0 = time.time()
                        algo.quicksortSeuil(array, 0, len(array) - 1)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortSeuilRandom"):
                        t0 = time.time()
                        algo.quicksortSeuilRandom(array, 0, len(array) - 1)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    #Append sorting time to an array
                    timeArray.append(algoTime)


            if folder_data[m] == "20_29":
                for j in range(20,30):
                    array = algo.fileToArray(folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt")
                    if (algoToDo[s] == "counting"):
                        t0 = time.time()
                        a = algo.counting_sort(array, max(array))
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if(algoToDo[s] == "quickSort"):
                        t0 = time.time()
                        a = algo.quickSort(array)
                        t1 = time.time()
                        algoTime = t1-t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortRandom"):
                        t0 = time.time()
                        a = algo.quickSortRandom(array)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortSeuil"):
                        t0 = time.time()
                        algo.quicksortSeuil(array, 0, len(array) - 1)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    if (algoToDo[s] == "quickSortSeuilRandom"):
                        t0 = time.time()
                        algo.quicksortSeuilRandom(array, 0, len(array) - 1)
                        t1 = time.time()
                        algoTime = t1 - t0

                        print(str(j) + " :" + str(algoTime))

                    #Append sorting time to an array
                    timeArray.append(algoTime)

            for k in range(0, 9):
                avg += timeArray[k]
            k = 0

            print("Average of " + data_dictionary[i] + ": " , avg/10)
            avgArr.append(avg/10)
            time_dictionary[data_dictionary[i]] = avg/10


        '''
        Temps vs taille
        '''
        plt.scatter(taille, avgArr)
        plt.suptitle(algoToDo[s] + ' for serie ' + folder_data[m], fontsize=20)
        plt.xlabel('Numer of data to sort', fontsize=18)
        plt.ylabel('Average sorting time', fontsize=16)
        plt.savefig(algoToDo[s] + '/time_' + folder_data[m] + '.png')
        plt.clf()

        '''
        Test de puissance
        echelle log-log
        '''
        plt.scatter(taille, avgArr)
        plt.xscale('log', linthreshy=0.01)
        plt.yscale('log', linthreshy=0.01)
        plt.title('Test de puissance')
        plt.grid(True)
        plt.savefig(algoToDo[s] + '/puissance_' + folder_data[m] + '.png')
        plt.clf()

        '''
        Test de rapport
        (x, y/f(x))
        '''
        rapportArr = []
        if(algoToDo[s] == "counting"):
            for x in range(0,6):
                rapportArr.append(avgArr[x]/taille[x])
            plt.scatter(taille, rapportArr)
            plt.title('Test du rapport')
            plt.grid(True)
            plt.savefig(algoToDo[s] + '/rapport_' + folder_data[m] + '.png')
            plt.clf()

        else:
            rapportArr = []
            for x in range(0,6):
                rapportArr.append(avgArr[x]/taille[x] * taille[x])

            plt.scatter(taille, rapportArr)
            plt.title('Test du rapport')
            plt.grid(True)
            plt.savefig(algoToDo[s] + '/rapport_n^2_' + folder_data[m] + '.png')
            plt.clf()

            rapportArr = []
            for x in range(0,6):
                rapportArr.append(avgArr[x]/taille[x] * math.log(taille[x]))

            plt.scatter(taille, rapportArr)
            plt.title('Test du rapport')
            plt.grid(True)
            plt.savefig(algoToDo[s] + '/rapport_nlogn_' + folder_data[m] + '.png')
            plt.clf()

        '''
        Test de constantes
        (f(x), y)
        '''
        constante = []
        if (algoToDo[s] == "counting"):
            for x in range(0, 6):
                constante.append(taille[x])
            plt.scatter(constante, avgArr)
            plt.title('Test du rapport')
            plt.grid(True)
            plt.savefig(algoToDo[s] + '/constantes_' + folder_data[m] + '.png')
            plt.clf()

        else:
            constante = []
            for x in range(0, 6):
                constante.append(taille[x] * taille[x])

            plt.scatter(constante, avgArr)
            plt.title('Test de constantes')
            plt.grid(True)
            plt.savefig(algoToDo[s] + '/constante_n^2_' + folder_data[m] + '.png')
            plt.clf()

            constante = []
            for x in range(0, 6):
                constante.append(taille[x] * math.log(taille[x]))

            plt.scatter(constante, avgArr)
            plt.title('Test de constantes')
            plt.grid(True)
            plt.savefig(algoToDo[s] + '/constante_nlogn_' + folder_data[m] + '.png')
            plt.clf()