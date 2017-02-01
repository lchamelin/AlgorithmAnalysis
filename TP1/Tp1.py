import os
import random
import time
import matplotlib



#matplotlib pour les graph
#ou csv


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

data_dictionary = {0: "1000", 1: "5000", 2: "10000", 3: "50000", 4: "100000", 5: "500000"}

for i in range(0,6):
    for j in range(0,10):
        t0 = time.time()
        a = insertionSort(fileToArray("INF4705_H17_TP1_donnees/0_9/testset_" + data_dictionary[i] + "_" + str(j) + ".txt"))
        t1 = time.time()
        print(data_dictionary[i] + " data: 0_9/" + str(j) + ": " + str(t1-t0))