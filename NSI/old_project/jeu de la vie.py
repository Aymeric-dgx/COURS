grille = [[0]*6 for i in range(6)]
grille[2][2]=1
grille[2][3]=1
grille[2][4]=1

def jeu_de_la_vie(grille):
    grille1=grille
    for i in range(1,len(grille)-1):
        for j in range(1,len(grille[i])-1):
            voisine=0
            for k in range(-1,2):
                for l in range(-1,2):
                    if k!=0 and l!=0:
                        if grille[i+k][j+l]==1:
                            voisine+=1
            if grille[i][j]==1 and (voisine==2 or voisine==3):
                grille[i][j]=1
            else:
                grille[i][j]=0
            if grille[i][j]==0 and voisine==3:
                grille[i][j]=1
            else:
                grille[i][j]=0
    return grille

