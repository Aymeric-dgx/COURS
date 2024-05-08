# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 21:41:23 2022

@author: Charles Clercq
"""
import time

def decoupeDeBarre(p, b) :
    '''
    #Resout le probleme de decoupe de barre pour maximiser les profits
    @ p : liste des profit par taille de barre
    @ b : taille de la barre d'origine
    $ retourne le nombre de découpe optimal
    '''
    if b == 0 :
        return 0
    else :
        maxi = -1
        for longueur in range(1,len(p)+1):
            if b >= longueur:
                maxi = max(maxi, p[longueur-1]+decoupeDeBarre(p, b - longueur))
        return maxi