#rech du nb d occurence d un caractere dans une chaine
def rechercher(car :str, ch : str, occ = 0):
    if len(ch) == 1:
        if ch[0] == car:
            occ = occ + 1
        return occ
    else:
        m = len(ch) // 2
        gauche = rechercher(car, ch[:m])
        droite = rechercher(car, ch[m:])
        occ = occ + gauche + droite
        return occ
    
l  = "abracadabra"
c = rechercher("b", l)
print(c)