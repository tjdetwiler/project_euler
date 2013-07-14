import numpy as np
import time
from fractions import Fraction


prevX = []
prevY = [1]

def print_set(Y):
    V = []
    for m in Y:
        V += Y[m]

    if len(V) != len(set(V)):
        print 'repeats in set!'
        print Y
    V.sort()
    for v in V:
        print v

    print "len = " + str(2*(len(V)-1)+1)


def get_len(Y):
    l = 0
    for m in Y:
        l += len(Y[m])
    return 2*(l-1)+1

def series(a,b):
    return (a*b)/(a+b)
    

def parallel(a,b):
    return a+b


def in_set(val,Y):
    for m in Y:
        if val in Y[m]:
            return 1
    return 0


def next_set(X,n):
    c = Fraction(1,1)
    Y = {}

    for m in X:
        if m not in Y:
            Y[m] = []
        if m+1 not in Y:
            Y[m+1] = []

        for v in X[m]:
            a = series(c,v)
            b = 1/parallel(c,v)

            # if n == 4: 
            #     print (a,b,v)
            if not in_set(a,Y):
                Y[m+1].append(a)

            if not in_set(b,Y):
                Y[m+1].append(b)

            if not in_set(v,Y):
                Y[m].append(v)


    keys = Y.keys()
    V = []
    for i in range(0,len(keys)):
        for j in range(i+1,len(keys)):
            ac = keys[i]
            bc = keys[j]
            if ac + bc == n and ac > 1 and bc > 1:

                for aa in Y[ac]:
                    for bb in Y[bc]:
                        yy = parallel(aa,bb)
                        if yy > 1:
                            yy = 1/yy
                        if not in_set(yy,Y):
                            # print (aa,ac,bb,bc,yy,n) 
                            V.append(yy)

    Y[n] += list(set(V))
    # keys = Y.keys()
    # for i in range(0,len(keys)):
    #     y = keys[i]
    #     Y[y] = list(set(Y[y]))
    #     Y[y].sort()

    return Y
        


def solve():
    n=1
    c = Fraction(1,1)
    X = {1:[c]}
    while n < 18:
        n += 1
        print "n = " + str(n) 
        X = next_set(X,n)
        # print_set(X)
        print 'len = ' + str(get_len(X)) 
        print "#############"       




if __name__ == "__main__":
    start = time.time()
    ans = solve()
    print "*****************"
    print ans
    stop=time.time()
    print "runtime: " + str(stop-start) + " sec."




# (2, 3, 3, 0, 3)
# (3, 7, 4, 0, 7)
# (4, 15, 8, 0, 15)
# (5, 35, 20, 4, 31)
# (6, 81, 46, 18, 63)
# (7, 193, 112, 66, 127)
# (8, 472, 279, 217, 255)
# (9, 1186, 714, 675, 511)
# (10, 2964, 1778, 1941, 1023)
# (11, 7487, 4523, 5440, 2047)
# (12, 18900, 11413, 14805, 4095)
# (13, 48049, 29149, 39858, 8191)
