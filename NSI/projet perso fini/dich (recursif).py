def dicho(l :list, v :int, d,  f)->tuple:
    m = (d+f)//2
    if v == l[m]:
        return (m, l[m])
    else:
        if v < l[m]:
            return dicho(l, v, d, m)
        else:
            return dicho(l, v, m+1, f)
        
l = [1,2,3,4,5,6,7,8,9,10]
c = dicho(l, 5, 0, len(l))
print(c)