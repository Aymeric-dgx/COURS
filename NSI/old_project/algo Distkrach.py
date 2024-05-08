graphe = {"a": [["b", 12], ["d", 14]],
           "b": [["a", 12], ["f", 9], ["h", 11], ["g", 16]],
            "c" : [["e"]] }



def init_dij(graphe, debut):
    distance = {sommet: 1E10 for sommet in graphe}
    predecesseur = {sommet: None for sommet in graphe}
    pas_visite = [sommet for sommet in graphe]
    distance[debut] = 0
    
    for i in range (len(graphe)):