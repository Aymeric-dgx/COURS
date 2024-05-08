p1 = ["1.8", "1.7", "1.6", "1.5", "1.4", "1.3", "1.2", "1.1"]
p2 = ["2.6", "2.5", "2.4", "2.3", "2.2", "2.1", "", ""]
p3 = ["3.2", "3.1", "", "", ""]
p4 = ["4.2", "4.1", "", "", "", "", "", "", ""]

liste_process = [p1, p2, p3, p4]

def choix_proc(liste_attente):
    if liste_attente != []:
        mini = len(liste_attente[0])
        indice = 0
        for i in range(1, len(liste_attente)):
            if len(liste_attente[i]) < mini:
                mini = len(liste_attente[i])
                indice = i
        return indice
    
def scrut(liste_proc):
    liste_attente = []
    for i in range(len(liste_proc)):
        if liste_proc[i] == []:
            pass
        elif liste_proc[i][-1] == "":
            liste_proc[i].pop(-1)
        else : 
            liste_attente.append(liste_proc[i])
    return liste_attente

def ordo(liste_proc):
    exec = []
    attente = scrut(liste_proc)
    while attente != []:
        indice = choix_proc(attente)
        proc = attente[indice].pop(-1)
        cycle = proc
        exec.append(cycle)
        attente = scrut(liste_proc)
    return exec

def somme_proc(liste_proc):
    somme = 0
    for i in range(len(liste_proc)):
        somme += len(liste_proc[i])
    return somme

def ordo2(liste_proc, quant):
    exec = []
    somme = somme_proc(liste_proc) #11
    
    if somme//2 == 1:
        somme = somme + 1   #12

    for j in range(somme//quant):  #6
        attente = scrut(liste_proc) #[[p1], [p2]]
        indice = choix_proc(attente)  #4

        for i in range(quant):
            if attente[indice] == True:
                proc = attente[indice].pop(-1)
                exec.append(proc)
            else:
                break
    
    return exec

print(ordo2(liste_process, 3))