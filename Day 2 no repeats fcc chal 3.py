# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 13:18:15 2019

@author: dan
"""

from itertools import permutations

def permAlone(string):
    totalPerms = [''.join(perm) for perm in permutations(string)]
    noRepeats = []
    
    for perm in totalPerms:
        #print(perm)
        neighbors = 0
        if len(perm) == 1:
            noRepeats.append(perm)
            print(len(noRepeats))
            #break
        else:
            for i in range(len(perm) - 1):
                if perm[i] == perm[i + 1]:
                    neighbors += 1
            if neighbors == 0:
                noRepeats.append(perm)
    return len(noRepeats)

print(permAlone("aaa"))
#0
print(permAlone("aabb"))
#8
print(permAlone("abcdefa"))
#3600
print(permAlone("abfdefa"))
#2640
permAlone("a")
#1
permAlone("aaab")
#0
