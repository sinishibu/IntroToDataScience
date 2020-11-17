# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:26:33 2020

@author: Sini
"""

def prevPermutation(str): 
      
    # Find index of the last element 
    # of the string 
    n = len(str) - 1
  
    # Find largest index i such that  
    # str[i ? 1] > str[i] 
    i = n 
    while (i > 0 and str[i - 1] <= str[i]): 
        i -= 1
  
    # if string is sorted in ascending order 
    # we're at the last permutation 
    if (i <= 0): 
        return False
  
    # Note - str[i..n] is sorted in  
    # ascending order 
  
    # Find rightmost element's index  
    # that is less than str[i - 1] 
    j = i - 1
    while (j + 1 <= n and 
           str[j + 1] <= str[i - 1]): 
        j += 1
  
    # Swap character at i-1 with j 
    str = list(str) 
    temp = str[i - 1] 
    str[i - 1] = str[j] 
    str[j] = temp 
    str = ''.join(str) 
  
    # Reverse the substring [i..n] 
    str[::-1] 
      
    return True, str
      
# Driver code 
if __name__ == '__main__': 
    str = "fjadchbegi"
      
    b, str = prevPermutation(str) 
      
    if (b == True): 
        print("Previous permutation is", str) 
    else: 
        print("Previous permutation doesn't exist") 