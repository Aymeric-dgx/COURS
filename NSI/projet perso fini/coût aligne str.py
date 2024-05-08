#en "bottom-up"

def aligne(s1 :str, s2 :str) -> int:
    mem = [[0]*(len(s1)+1) for _ in range(len(s2)+1)]
    for i in range(len(s1)+1):
        mem[0][i] = i
    for i in range(len(s2)+1):
        mem[i][0] = i
    
    for i in range(1, len(s2)+1):
        for j in range(1, len(s1)+1):
            val = 0
            if s1[j-1] != s2[i-1]:
                val = 1
            mem[i][j] = min(mem[i-1][j-1]+val, mem[i-1][j]+1, mem[i][j-1]+1)
    return mem[-1][-1]

s1 = "SSQDA"
s2 = "BDDQSDCSDAAA"
c = aligne(s1, s2)
print(c)


