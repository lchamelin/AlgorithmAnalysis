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


a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print("QuickSort pivot = 1 ")
print("Before: ")
print(a)
a = quickSort(a)
print("After:")
print(a)

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print("QuickSort pivot = random ")
print("Before: ")
print(a)
a = quickSortRandom(a)
print("After:")
print(a)

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
print("InsertionSort")
print("Before: ")
print(a)
a = insertionSort(a)
print("After:")
print(a)
