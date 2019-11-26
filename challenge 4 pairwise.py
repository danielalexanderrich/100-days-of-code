# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 20:40:51 2019

@author: dan
"""

def pairwise(array, num):
    ogArray = array.copy()
    for element in array:
        compArray = array.copy()
        compArray.remove(element)
        for i in range(len(compArray)):
            if element + compArray[i] == num:
                if array.count(element) == 1:
                    print(array.index(element), array.index(compArray[i]))
                else:
                    array.remove(element)
                    print(array.index(element), array.index(compArray[i]))
                
print(pairwise([1,2,3,4,0,2],4))