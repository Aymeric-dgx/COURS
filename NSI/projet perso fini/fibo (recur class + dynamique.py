import time

def fibo(x):
    if x<2 :
        return x
    else:
        return fibo(x-1) + fibo(x-2)
    
def fibo2(x):
    m  = [-1]*(x+1)
    def sub_fibo(x,m):
        if x<2:
            return x
        elif m[x]>-1:
            return m[x]
        else:
            m[x] = sub_fibo(x-1, m) + sub_fibo(x-2, m)
            return m[x]
    return sub_fibo(x,m)
        

s = time.time()
print(fibo(30))
print(time.time()-s)

s1 = time.time()
print(fibo2(500))
print(time.time()-s1)
