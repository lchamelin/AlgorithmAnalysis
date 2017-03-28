import time
import sys

#Set the recursion limit
sys.setrecursionlimit(100000)

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
