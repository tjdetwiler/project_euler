import numpy as np
from fractions import Fraction


prevX = []
prevY = [1]

def print_list(X):
    XX = list(set([ a for (a,b) in X]))
    XX.sort()
    print "len: " + str(len(XX))
    for x in XX:
        print x
    print "#############"

def print_new(X):
    global prevX
    global prevY

    XX = list(set([ a for (a,b) in X]))
    XX.sort()
    print "len: " + str(len(XX))
    Y = []
    for x in XX:
        if x not in prevX:
            print x
            Y.append(x)

    predicted = [] 
    for y in prevY:
        predicted.append(Fraction(y.numerator,y.numerator+y.denominator))   
    for y in Y:
        if y not in predicted and y < Fraction(1,1):
           print y
           pass

    prevX = XX
    prevY = Y





def series(a,b):
    return (a*b)/(a+b)
    

def parallel(a,b):
    return a+b

def next_set(X,n):
    Y = []
    c = Fraction(2,1)
    V = []
    for (x,y) in X:
        Y.append( (series(c,x),y+1) )
        Y.append( (parallel(c,x),y+1) )
        Y.append( (x,y) )
        V.append(series(c,x))
        V.append(parallel(c,x))
        V.append(x)


    for i in range(0,len(X)):
        for j in range(i+1,len(X)):
            (a,ac) = X[i]
            (b,bc) = X[j]
            if ac + bc <= n and ac > 1 and bc > 1:
                yy = series(a,b)
                if yy not in V:
                    print (a,b,yy,"series")
                    Y.append( (series(a,b),ac+bc) )
                yy = parallel(a,b)
                if yy not in V:
                    print (a,b,yy,"parallel")
                    Y.append( (parallel(a,b),ac+bc) )
    Y = list(set(Y))                

    return Y
        

def solve():
    n=1
    c = Fraction(2,1)
    X = [(c,1)]
    while n < 7:
        n += 1
        X = next_set(X,n)
        print "n = " + str(n) 
        print len(X)
        # print_new(X)
        print "#############"       







if __name__ == "__main__":
    ans = solve()
    print "*****************"
    print ans


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
