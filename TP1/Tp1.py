import os
import random
import time
#import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

class SortingAlgorithme:

    '''
    Counting Sort
    Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Counting_sort#Python
    '''
    def counting_sort(self, array, maxval):
        """in-place counting sort"""
        m = maxval + 1
        count = [0] * m               # init with zeros
        for a in array:
            count[a] += 1             # count occurences
        i = 0
        for a in range(m):            # emit
            for c in range(count[a]): # - emit 'count[a]' copies of 'a'
                array[i] = a
                i += 1
        return array

    '''
    #Quick Sort avec un pivot au premier element
    # Source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
    '''
    def quickSort(self, arr):
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
            less = self.quickSort(less)
            more = self.quickSort(more)
            return less + pivotList + more


    '''
    #Quick Sort avec un pivot aleatoire
    '''
    def quickSortRandom(self, arr):
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
            less = self.quickSort(less)
            more = self.quickSort(more)
        return less + pivotList + more


    '''
    #Insertion sort
    '''
    def insertionSort(self, my_list):
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
    #Read file and append data to a list
    '''

    def quicksortSeuil(self, numList, first, last):
        m = 10
        if first < last:
            sizeArr = last - first + 1
            if (sizeArr < m):
                self.insert_sort(numList, first, last)
            else:
                mid = self.partition(numList, first, last)
                self.quicksortSeuil(numList, first, mid - 1)
                self.quicksortSeuil(numList, mid + 1, last)


    def partition(self, numList, first, last):
        piv = numList[first]
        i = first - 1
        for j in range(first, last):
            if numList[j] < piv:
                i += 1
                temp = numList[i]
                numList[i] = numList[j]
                numList[j] = temp

        tempo = numList[i + 1]
        numList[i + 1] = numList[last]
        numList[last] = tempo

        return i + 1

    def quicksortSeuilRandom(self, numList, first, last):
        m = 10
        if first < last:
            sizeArr = last - first + 1
            if (sizeArr < m):
                self.insert_sort(numList, first, last)
            else:
                mid = self.partitionRandom(numList, first, last)
                self.quicksortSeuil(numList, first, mid-1 )
                self.quicksortSeuil(numList, mid + 1, last)


    def partitionRandom(self, numList, first, last):
        piv = random.randint(0, len(numList))
        i = first - 1
        for j in range(first, last):
            if numList[j] < piv:
                i += 1
                temp = numList[i]
                numList[i] = numList[j]
                numList[j] = temp

        tempo = numList[i + 1]
        numList[i + 1] = numList[last]
        numList[last] = tempo

        return i + 1


    def insert_sort(self, numList, first, last):
        for x in range(first, last + 1):
            key = numList[x]
            y = x - 1
            while y > -1 and numList[y] > key:
                numList[y + 1] = numList[y]
                y = y - 1
            numList[y + 1] = key


    def fileToArray(self, file):
        with open(file, "r") as ins:
            array = []
            for line in ins:
                array.append(int(line))

            return array

algo = SortingAlgorithme()

if(sys.argv[1] == "quick"):
    print("Here")
    array = algo.fileToArray(str(sys.argv[2]))
    t0 = time.time()
    array = algo.quickSort(array)
    t1 = time.time()

elif (sys.argv[1] == "quickRandom"):
    print("Here")
    array = algo.fileToArray(str(sys.argv[2]))
    t0 = time.time()
    array = algo.quickSortRandom(array)
    t1 = time.time()

elif (sys.argv[1] == "counting"):
    print("Here")
    array = algo.fileToArray(str(sys.argv[2]))
    t0 = time.time()
    array = algo.counting_sort(array, max(array))
    t1 = time.time()

elif (sys.argv[1] == "quickSeuil"):
    print("Here")
    array = algo.fileToArray(str(sys.argv[2]))
    t0 = time.time()
    algo.quicksortSeuil(array, 0, len(array) - 1)
    t1 = time.time()

elif (sys.argv[1] == "quickRandomSeuil"):
    print("Here")
    array = algo.fileToArray(str(sys.argv[2]))
    t0 = time.time()
    algo.quicksortSeuilRandom(array, 0, len(array) - 1)
    t1 = time.time()



algoTime = t1-t0

if(len(sys.argv) >= 4):
    if(sys.argv[3] == "-p"):
        for elem in array:
            print(elem)

    if((sys.argv[3] == "-t")):
        print(algoTime)

    if(len(sys.argv) >= 5):
        if(sys.argv[4] == "-p"):
            for elem in array:
                print(elem)

        elif((sys.argv[4] == "-t")):
            print(algoTime)


