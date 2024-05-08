#eucl(r, u, v, 0, u', v') = (r, u, v)
#eucl(r, u, v, r', u', v') = eucl(r', u', v', r - (r÷r')*r', u - (r÷r')*u', v - (r÷r')*v')  pour r' ≠ 0
#euclid(a, b) = eucl(a, 1, 0, b, 0, 1)

def eucl(r, u, v, r_, u_, v_):
    if r_ == 0:
        return (r, u, v)
    else :
        return eucl(r_, u_, v_, r - (r//r_)*r_, u - (r//r_)*u_, v - (r//r_)*v_)

def euclide(a, b):
    return eucl(a, 1, 0, b, 0, 1)

if __name__ == '__main__':

    a = 8
    b = 3
    pgcd, bu, bv = euclide(a, b)
    print('PGCD :', pgcd)
    print('Coeficients de Bezout :', bu, bv)
    print('r = a*u+b*v ->', pgcd, '=',a,'*',bu,'+',b,'*',bv)

