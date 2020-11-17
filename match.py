# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 16:34:54 2020

@author: Sini
"""

games = {'match1': {'plr1': 15, 'plr2': 25}, 'match2': {'plr2': 30, 'plr3': 40}}
def orangecap (d):
    totalscore = dict()
    for match in d:
        for plr in d[match]:
            if plr in totalscore:
                totalscore[plr] += d[match][plr]
            else:
                totalscore[plr] = d[match][plr]
    best = max(totalscore, key=totalscore.get)
    return best, totalscore[best]
    
print(findbestplr(games))