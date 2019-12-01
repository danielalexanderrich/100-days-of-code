# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 20:19:54 2019

@author: dan
"""

def selectionSort(array):
    newArray = []
    i = len(array)
    while i > 0:
        smallest = array.pop(array.index(min(array)))
        newArray.append(smallest)
        i = len(array)
    return newArray
