import os
import random
import time
#import matplotlib.pyplot as plt
import sys

sys.setrecursionlimit(100000)

class SortingAlgorithme:

    # Counting Sort
    # Source: https://en.wikibooks.org/wiki/Algorithm_Implementation/Sorting/Counting_sort#Python
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

    # Quick Sort avec un pivot au premier element
    # Source: https://rosettacode.org/wiki/Sorting_algorithms/Quicksort#Python
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


    # Quick Sort avec un pivot aleatoire
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


    # QuickSort avec un seuil
    def quicksortSeuil(self, numList, first, last):
        left = first - 1
        right = last + 1
        pivot = numList[first]
        seuil = 10

        if ((last - first) < seuil):
            self.insert_sort(numList, first, last)
            return

        while True :
            right = right - 1
            while numList[right] > pivot:
                right = right - 1

            left = left + 1
            while numList[left] < pivot:
                left = left + 1

            if left < right:
                temp = numList[left]
                numList[left] = numList[right]
                numList[right] = temp
            else:
                break
        self.quicksortSeuil(numList, first, right)
        self.quicksortSeuil(numList, right+1, last)

    # QuickSort avec un seuil et un pivot random
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

    #
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

    # Insertion sort
    def insert_sort(self, numList, first, last):
        for x in range(first, last + 1):
            key = numList[x]
            y = x - 1

            while y > -1 and numList[y] > key:
                numList[y + 1] = numList[y]
                y = y - 1
            numList[y + 1] = key

    # Ajoute tout le data present dans le fichier choisi a un array pour ensuite le trier
    def fileToArray(self, file):
        with open(file, "r") as ins:
            array = []
            for line in ins:
                array.append(int(line))

            return array

############################################################################
############################################################################

# instantiation dun algo de la class SortingAlgorithme
algo = SortingAlgorithme()

# Switch case qui permet de choisir le bon algo en fonctione des parametres
# passes au terminal par le user

if(sys.argv[1] == "quick"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    array = algo.quickSort(array)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "quickRandom"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    array = algo.quickSortRandom(array)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "counting"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    array = algo.counting_sort(array, max(array))
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "quickSeuil"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    algo.quicksortSeuil(array, 0, len(array) - 1)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()

elif (sys.argv[1] == "quickRandomSeuil"):
    array = algo.fileToArray(str(sys.argv[2]))
    # Debuter le calcul de temps
    t0 = time.time()
    algo.quicksortSeuilRandom(array, 0, len(array) - 1)
    # Prendre le temps que l'algo a prit pour sort
    t1 = time.time()


# calcul du temps pour l'execution de lalgo choisi.
algoTime = t1-t0

# Switch case pour gerer les options entrer au teminal
# Si un 'P' est entrer, les donnees seront imprime triees au terminal
# Si un 't' est entrer, le temps d'execution de tri sera imprime au terminal
if(len(sys.argv) >= 4):
    # Si 'p' est entre
    if(sys.argv[3] == "-p"):
        for elem in array:
            print(elem)
    # Si 't' est entre
    elif((sys.argv[3] == "-t")):
        print(algoTime)

    if(len(sys.argv) >= 5):
        # Si 'p' est entre
        if(sys.argv[4] == "-p"):
            for elem in array:
                print(elem)
        # Si 't' est entre
        elif((sys.argv[4] == "-t")):
            print(algoTime)

