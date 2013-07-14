import time
import numpy as np
import matplotlib.pyplot as plt

#runtime ~44 sec

def sx(x):
    ceilx = np.ceil(x)
    below = x - np.floor(x)
    above = ceilx - x
    # print (x,above,below)
    if below < above:
        return below
    return above

def blanc(x):
    w = 0.5
    y = sx(x)
    n = 1
    increment = 1
    while increment > 1e-9:
        z = (2**n)*x
        increment = (w**n)*sx(z)
        y += increment
        n +=1 
    return y        
    
def get_roots():
    a = 0.0789080000001
    a = 0.0789077879996
    a = 0.078907788
    b = 0.499999999997
    b = 0.5
    return (a,b)

def find_roots():
    X= []
    Y = []
    x = 0.07889
    y = 0
    while x < .07891:
        x += .0000000001
        B = blanc(x)
        y = B**2 - B + x**2 - 0.5*x + 0.25
        X.append(x)
        Y.append(abs(y))
    print len(Y)
    print min(Y)
    print Y.index(min(Y))
    print X[Y.index(min(Y))]
    plt.plot(X,Y)
    plt.show()


def val_of_circle(x):
    return 0.5 - np.sqrt((1./16.) - (x-0.25)**2)


def reimann_sum(a,b):
    x = a
    S = 0
    dx = 0.000003

    while x < b:

        s =  (blanc(x)-val_of_circle(x))*dx
        if s < 0:
            continue

        S += s
        x += dx
    print "Riemann Sum Val: " + str((b,S))
    return S 



def solve():
    (a,b) = get_roots()
    v = reimann_sum(a,b)
    # vv = .25 - v 
    # ww = area_under_circle(a,b)
    # print (vv,ww)
    # return vv -ww
    return v



if __name__== "__main__":
  start = time.time()
  ans = solve()
  print "**************"
  print ans
  stop = time.time()
  print "runtime: " + str(stop-start)
