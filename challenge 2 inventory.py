# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 12:12:14 2019

@author: dan
"""

curInv = [
        [21, "Bowling Ball"],
        [2, "Dirty Sock"],
        [1, "Hair Pin"],
        [5, "Microphone"]
        ]

newInv = [
    [2, "Hair Pin"],
    [3, "Half-Eaten Apple"],
    [67, "Bowling Ball"],
    [7, "Toothpaste"]
]

def takeSecond(elem):
    return elem[1]

def updateInventory(arr1, arr2):
    newItem = []
    for i in range(len(arr2)):
        matchTally = 0
        for j in range(len(arr1)):
            if arr2[i][1] == arr1[j][1]:
                arr1[j][0] = arr1[j][0] + arr2[i][0]
                matchTally += 1
        if matchTally == 0:
            newItem.append(arr2[i])
    for item in newItem:
        arr1.append(item)
    arr1.sort(key = takeSecond)
    return arr1
            
print(updateInventory(curInv, newInv))

print(updateInventory([[21, "Bowling Ball"],
                       [2, "Dirty Sock"], 
                       [1, "Hair Pin"],
                       [5, "Microphone"]], []))
            