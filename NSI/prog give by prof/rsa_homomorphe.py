# Créé par charles.clercq, le 01/12/2023 en Python 3.7
from algorithme_Euclide_etendu import euclide

p = 53#101#40009#3
q = 97#997#49999#5
n = p*q
phi = (p-1)*(q-1)
e = 2
r, u, v = euclide(phi, e)
while r != 1 :
    e = e + 1
    r, u, v = euclide(phi, e)
d = v

deux = (2**e)%n
trois = (3**e)%n
six = deux * trois

print('six :', six, '->', (six**d)%n)
