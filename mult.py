# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 18:18:14 2020

@author: Sini
"""
def remdup(x):
    res = [] 
    for i in x: 
        if i not in res: 
            res.append(i)
    return res
arr=input()
arr=arr.split()
for i in range(len(arr)) : 
    arr[i] = int(arr[i]) 
mylist=remdup(arr)
print(mylist)
 