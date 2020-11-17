# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 12:26:11 2020

@author: Sini
"""

def repfree(x):
    flag=0
    p=len(x)
    for i in range(0,p-1):
        b=x[i]
        for j in range(i+1,p-1):
            if x[j]==b:	
                flag=1
                break
                
                  		
    if flag==1:
    	return("False")
    else:
        return ("True")