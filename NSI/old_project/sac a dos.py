obj = {"A" : [13, 700],"Z" : [5,7000], "B" : [12, 400], "C" : [8, 300], "D" : [10, 300]} # [poids, valeur]
cap = 30 # capacité du sac

def backPack(obj, cap):
    val = 0
    poids_courant = 0
    def aux(obj, cap, poids_courant, sac = [], tmp_val = 0):
        for objets in obj:
            if not objets in sac:
                if poids_courant + obj[objets][0] <= cap:
                    tmp_val = max(0, obj[objets][1] + aux(obj, cap, poids_courant + obj[objets][0],  sac + [objets]))
        return tmp_val
    return aux(obj, cap, poids_courant)

print(backPack(obj, cap)) # 1000

#marche pas