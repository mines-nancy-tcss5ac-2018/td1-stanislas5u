
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:14:42 2018

@author: rambaud5u
"""

def solve(n):
    P = 2**n
    L = str(P)
    S = 0
    for i in range(len(L)):
        S = S + int(L[i])
    return S

print(solve(1000))
