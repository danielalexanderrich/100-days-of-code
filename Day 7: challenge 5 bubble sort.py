# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 17:06:49 2019

@author: Daniel
"""

def bubbleSort(array):
    for i in range(len(array)):
        print("comparing {}".format(array[i]))
        for j in range(len(array)):
            print("to {}".format(array[j]))
            if array[i] < array[j]:
                print("swapping {} and {}".format(array[i], array[j]))
                array[i], array[j] = array[j], array[i]
    
    
    return array
