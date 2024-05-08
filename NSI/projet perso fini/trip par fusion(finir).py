def triFusion(lg :list, ld :list, lt =[]):
    def tri(lg,ld):
        for i in range(len(lg)):
            for j in range(len(lg)):
                if lg[i]<lg[j]:
                    lg[i], lg[j] = lg[j], lg[i]
        for i in range(len(ld)):
            for j in range(len(ld)):
                if ld[i]<ld[j]:
                    ld[i], ld[j] = ld[j], ld[i]
    tri(lg,ld)
    if lg == [] and ld == []:
        return lt
    elif lg == []:
        return lt + ld
    elif ld == []: 
        return lg + lt
    else:
        if lg[0] < ld[0]:
            lt = lt + [lg[0]]
            return triFusion(lg[1:], ld, lt)
        else:
            lt = lt + [ld[0]]
            return triFusion(lg, ld[1:], lt)
        
l1 = [3,5,8,14]
l2 = [1,2,4,6,7,71,18]
c = triFusion(l1, l2)
print(c)