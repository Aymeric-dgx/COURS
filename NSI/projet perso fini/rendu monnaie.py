#rendu monnaie recursif

def rendu(val, rend =[], pieces = [200, 100, 50, 20, 10, 5, 2, 1]):
    if val == 0:
        return rend
    else:
        for p in pieces:
            if p <= val:
                rend.append(p)
                return rendu(val - p, rend, pieces)
        return rend
    
#rendu monnaie dynamique "top down"

def rendu_dyn(val, pieces = [200, 100, 50, 20, 10, 5, 2, 1]):
    m = [-1]*(val+1)
    m[0] = [0]
    rend = []
    def rendu_sub(val, pieces, m):
        if m[val] != -1:
            return m[val]
        elif val == 0:
            return []
        else:
            for i in range(len(pieces)):
                if pieces[i] <= val:
                    c = rendu_sub(val-pieces[i], pieces, m)
                    if m[val] == -1 or len(c) < len(m[val]):
                        m[val] = c+[pieces[i]]
            return m[val]
    rendu = rendu_sub(val, pieces, m)
    return rendu[1:]

c = rendu_dyn(173)
print(c)