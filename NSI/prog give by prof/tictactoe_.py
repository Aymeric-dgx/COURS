#tic tac toe

def gagne(un_plateau : list, joueur : int) :
    for i in range(3) :
        if un_plateau[3*i:3*i+3] == [joueur, joueur, joueur]:
            return True
        elif [un_plateau[i], un_plateau[i+3], un_plateau[i+6]] == [joueur, joueur, joueur]:
            return True
    if [un_plateau[0], un_plateau[4], un_plateau[8]] == [joueur, joueur, joueur]:
        return True
    elif [un_plateau[2], un_plateau[4], un_plateau[5]] == [joueur, joueur, joueur]:
        return True
    return False

def play(un_plateau : list, joueur : int, courant : int, profondeur : int) :
	pass

if __name__ == "__main__" :
    plateu_1 = [1,1,1,0,0,0,0,0,0]
    assert gagne(plateu_1, 1) == True, 'Error ligne 1'
    plateu_2 = [0,0,0,1,1,1,0,0,0]
    assert gagne(plateu_2, 1) == True, 'Error ligne 2'
    plateu_3 = [0,0,0,0,0,0,1,1,1]
    assert gagne(plateu_3, 1) == True, 'Error ligne 3'

    plateu_4 = [1,0,0,1,0,0,1,0,0]
    assert gagne(plateu_4, 1) == True, 'Error col 1'
    plateu_5 = [0,1,0,0,1,0,0,1,0]
    assert gagne(plateu_5, 1) == True, 'Error col 2'
    plateu_6 = [0,0,1,0,0,1,0,0,1]
    assert gagne(plateu_6, 1) == True, 'Error col 3'

    plateu_7 = [1,0,0,0,1,0,0,0,1]
    assert gagne(plateu_7, 1) == True, 'Error diag 1'
    plateu_8 = [0,0,1,0,1,0,1,0,0]
    assert gagne(plateu_7, 1) == True, 'Error diag 2'