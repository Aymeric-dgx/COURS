def rechMin(l :list):
    if len(l) == 1:
        return l[0]
    else:
        vg = rechMin(l[:len(l)//2])
        vd = rechMin(l[len(l)//2:])
        if vg < vd:
            return vg
        else:
            return vd
        
l = [5,14,2,68,145,1,25,1,425]
c = rechMin(l)
print(c)