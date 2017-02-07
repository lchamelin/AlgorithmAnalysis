import os
import random
import time
import matplotlib.pyplot as plt
import sys



'''
Quick Sort avec un pivot au premier element
# Source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
'''
def quickSort(arr):
    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more


'''
Quick Sort avec un pivot aleatoire
'''
def quickSortRandom(arr):
    less = []
    pivotList = []
    more = []
    randomPivot = random.randint(0, len(arr))
    #print(randomPivot)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[randomPivot]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
    return less + pivotList + more


'''
Insertion sort
'''
def insertionSort(my_list):
    for i in range(1, len(my_list)):

        val_current = my_list[i]
        pos = i

        # check backwards through sorted list for proper pos of val_current
        while ((pos > 0) and (my_list[pos - 1] > val_current)):
            my_list[pos] = my_list[pos - 1]
            pos = pos - 1

        if pos != i:
            my_list[pos] = val_current

    return my_list


'''
Read file and append data to a list
'''
def fileToArray(file):
    with open(file, "r") as ins:
        array = []
        for line in ins:
            array.append(line)
        return array


if(sys.argv[0] == "quick"):
    quickSort(fileToArray(str(sys.argv[1])))

'''
Dictionaries to call all files in all folder
'''
'''
data_dictionary = {0: "1000", 1: "5000", 2: "10000", 3: "50000", 4: "100000", 5: "500000"}
time_dictionary = {"1000" : 0, "5000" : 0, "10000" : 0, "50000" : 0, "100000" : 0, "500000" : 0}
folder_data = {0: "0_9", 1: "10_19", 2: "20_29"}
'''

'''
All set of data in all folder
'''
'''
for m in range(2,3):
    print("Folder " + folder_data[m] + ":")
    for i in range(0,6):
        timeArray = []
        avg = 0

        if folder_data[m] == "0_9":
            for j in range(0,9):
                t0 = time.time()
                a = quickSort(fileToArray("INF4705_H17_TP1_donnees/" + folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt"))
                t1 = time.time()
                algoTime = t1-t0

                #Append sorting time to an array
                timeArray.append(algoTime)

        if folder_data[m] == "10_19":
            for j in range(10,19):
                t0 = time.time()
                a = quickSort(fileToArray("INF4705_H17_TP1_donnees/" + folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt"))
                t1 = time.time()
                algoTime = t1-t0

                #Append sorting time to an array
                timeArray.append(algoTime)

0_9/testset_1000_1.txt
        if folder_data[m] == "10_19":
            for j in range(10,19):
                t0 = time.time()
                a = quickSort(fileToArray("INF4705_H17_TP1_donnees/" + folder_data[m] + "/testset_" + data_dictionary[i] + "_" + str(j) + ".txt"))
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
    plt.suptitle('Data in serie 10_19', fontsize=20)
    plt.xlabel('Numer of data to sort', fontsize=18)
    plt.ylabel('Average sorting time', fontsize=16)
    plt.savefig('data' + folder_data[m] + '.png')
'''