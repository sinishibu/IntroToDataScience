# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:10:05 2020

@author: Sini
"""

n=int(input())
arr=[]
rev=[]
sum=[]
for i in range(0, n):    
    arr.insert(i,int(input()))

for j in range(n-1, -1, -1):     
    rev.insert(i,arr[j])

for k in range(0, n):    
    sum.insert(i,arr[k]+rev[k])
print(sum)


    
