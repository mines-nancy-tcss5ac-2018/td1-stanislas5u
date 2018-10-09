# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 15:28:20 2018

@author: rambaud5u
"""


def val(mot):
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    somme = 0
    for lettre in mot:
        indice=1
        for j in alphabet:
            if lettre == j:
                somme += indice
            else:
                indice += 1
    return somme
        
    
f = open('p022_names.txt', 'r')
str(f).split(",")
L = sorted(f)

def solve(f):
    s = 0
    for i in range(len(f)):
        for j in range(len(f[i])):
            s = s + val(f[i][j])*j
    return s


print(solve(L)) 
    
#l'algorithme affiche une valeur assez élevée mais je ne comprends pas pourquoi


