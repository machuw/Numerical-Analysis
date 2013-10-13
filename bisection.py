def sgn(x):
    ''' use signum function gives the same result,
        but avoids the possibility of overflow or underflow '''
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def bisection0(func, a, b, TOL=0.0001, N=100):
    ''' stopping criteria: |p - p(n)| < |b(n)- a(n)|/2 < TOL '''
    a = float(a)
    b = float(b)
    FA = func(a)
    i = 1
    while i < N:
        p = a + (b - a)/2
        FP = func(p)
        if (p == 0) or ((b-a)/2 < TOL):
            print("Method success after N iteration, N=%d" % i)
            return p
        if sgn(FA)*sgn(FP) > 0:
            a = p
            FA = func(p)
        else:
            b = p
        i = i+1   
    print("Method failed after N iteration, N=%d" % N)
    return

def bisection1(func, a, b, TOL=0.0001, N=100):
    ''' stopping criteria: |p - p(n)|/|p| < |b(n+1) - a(n+1)|/|a(n+1)| < TOL '''
    a = float(a)
    b = float(b)
    FA = func(a)
    i = 1
    while i < N:
        p = a + (b - a)/2
        FP = func(p)
        if (p == 0):
            print("Method success after N iteration, N=%d" % i)
            return p
        if sgn(FA)*sgn(FP) > 0:
            a = p
            FA = func(p)
        else:
            b = p
        if (b - a)/a < TOL:
            print("Method success after N iteration, N=%d" % i)
            return p
        i = i+1   
    print("Method failed after N iteration, N=%d" % N)
    return


