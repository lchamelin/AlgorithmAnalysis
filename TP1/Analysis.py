import os
import random
import time
import matplotlib.pyplot as plt
import sys
import Tp1 as algo

sys.setrecursionlimit(100000)
algo = algo.SortingAlgorithme()


'''
Dictionaries to call all files in all folder
'''

data_dictionary = {0: "1000", 1: "5000", 2: "10000", 3: "50000", 4: "100000", 5: "500000"}
time_dictionary = {"1000" : 0, "5000" : 0, "10000" : 0, "50000" : 0, "100000" : 0, "500000" : 0}
folder_data = {0: "0_9", 1: "10_19", 2: "20_29"}


'''
All set of data in all folder
'''

for m in range(0,3):
    print("Folder " + folder_data[m] + ":")
    for i in range(0,6):
        timeArray = []
        avg = 0

        if folder_data[m] == "0_9":
            for j in range(1,10):
                array = algo.fileToArray(folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt")
                t0 = time.time()
                a = algo.quickSort(array)
                t1 = time.time()
                algoTime = t1-t0

                print(str(j) + " :" + str(algoTime))

                #Append sorting time to an array
                timeArray.append(algoTime)

        if folder_data[m] == "10_19":
            for j in range(10,19):
                array = algo.fileToArray(folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt")
                t0 = time.time()
                a = algo.quickSort(array)
                t1 = time.time()
                algoTime = t1-t0

                print(str(j) + " :" + str(algoTime))
                #Append sorting time to an array
                timeArray.append(algoTime)


        if folder_data[m] == "20_29":
            for j in range(20,29):
                array = algo.fileToArray(folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt")
                t0 = time.time()
                a = algo.quickSort(array)
                t1 = time.time()
                algoTime = t1-t0

                #Append sorting time to an array
                timeArray.append(algoTime)

        for k in range(0, 9):
            avg += timeArray[k]
        k = 0

        print("Average of " + data_dictionary[i] + ": " , avg/10)
        time_dictionary[data_dictionary[i]] = avg/10

    plt.bar(range(len(time_dictionary)), time_dictionary.values(), align='center')
    plt.xticks(range(len(time_dictionary)), list(time_dictionary.keys()))
    plt.suptitle('Data in serie ' + folder_data[m], fontsize=20)
    plt.xlabel('Numer of data to sort', fontsize=18)
    plt.ylabel('Average sorting time', fontsize=16)
    plt.savefig('quickSort_' + folder_data[m] + '.png')
