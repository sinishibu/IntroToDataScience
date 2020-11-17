# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:05:30 2020

@author: Sini
"""

A=[]
B=[]
C=[]
A=input().split()
for i in range(0,len(A)):
  A[i]=int(A[i])
A.sort()

for j in range(0,len(A)):
  if(A[j]!=-1):
      B.append(A[j])

for k in range(0,len(A)):
    if(k in B):
        C.append(k)
    else:
        C.append(-1)
  
for i in range(0,len(A)):
  print(C[i],end=" ")