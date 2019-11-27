# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 11:39:04 2019

@author: dan
"""

def sym(*arrays):
    result = []
    for i in range(len(arrays)):
        uniquearray = list(set(arrays[i]))
        for j in range(len(uniquearray)):
            result.append(uniquearray[j])
    repeatdict = {x: result.count(x) for x in result if result.count(x) > 1}
    repeated = list(repeatdict.keys())
    result = list(set(result) - set(repeated))
    print(result)
    return result


#Unit tests
    
sym([1, 2, 3], [5, 2, 1, 4])
sym([1, 2, 3], [5, 2, 1, 4])
sym([1, 2, 3, 3], [5, 2, 1, 4])
sym([1, 2, 3, 3], [5, 2, 1, 4])
sym([1, 2, 3], [5, 2, 1, 4, 5])
sym([1, 2, 3], [5, 2, 1, 4, 5])
sym([1, 2, 5], [2, 3, 5], [3, 4, 5])
sym([1, 2, 5], [2, 3, 5], [3, 4, 5])
sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])
sym([1, 1, 2, 5], [2, 2, 3, 5], [3, 4, 5, 5])
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3])
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])
sym([3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1])


#ugh there is an error; it just checks for repeated, not if its in the set
# try using sets earlier maybe? idk
























