def machineDeTuring(bande:list, etats:dict, etat : str, index : int) -> list:
    while etat != "":
        val = bande[index]
        bande[index] = etats[etat][val][0]
        index = index + etats[etat][val][1]
        etat = etats[etat][val][2]

    return bande

#faire un dic comp_1 et comp_2 pour utiliser la machine de turing pour les deux complémentaires
#compe_1 = transformer les 1 en 0 et inversement
#comp_2 = faire comp_1 et ajouter 1 au rsesultat (binaires)  -> ce que fait le dict donne par le prof


if __name__ == '__main__' :
    ma_bande_infini = [-1, 0, 1, 1, 1, -1]
    mes_etats = {'e0' : {0 : [0, 1, 'e0'], 1 : [1, 1, 'e0'], -1 : [-1, -1, 'e1']},
    'e1' : {0 : [1, -1, 'e2'], 1 : [0, -1, 'e1'], -1 : [-1, 1, '']},
    'e2' : {0 : [0, -1, 'e2'], 1 : [1, -1, 'e2'], -1 : [-1, 1, '']}}
    etat_depart = 'e0'
    index_bande = 1
    assert machineDeTuring(ma_bande_infini, mes_etats, etat_depart, index_bande) == [-1, 1, 0, 0, 0, -1]

