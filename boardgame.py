# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:38:40 2020

@author: Sini
"""

import random
def play(psn):
    r=random.randint(1,6)
    print("Dice rolled:",r)
    input()
    if(psn==0):
        if(r==1 or r==6):
            psn=1
    else:
            psn=psn+r
    print("Position=", psn)
    if(psn>=100):
        print("You won")
        return
    play(psn)
position=0
print("Position=",position)
play(position)