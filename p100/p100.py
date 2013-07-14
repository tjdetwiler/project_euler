import itertools
import numpy as np
from fractions import Fraction
import time

def solve():

    b = int(10**12)
    b = 5
    c = 0
    f2 = Fraction(1,2)
    mf = float('inf')
    sqrt2 = np.sqrt(2)
    last = 4
    while True:
        a = int(np.ceil(b/sqrt2))
        d = Fraction(int(a*(a-1)),int(b*(b-1)))

        if d == f2:
            x = float(b)/last
            last = b
            if b > int(1e12):
                return a
            b = int(b*x)
         
        c += 1
        b += 1



        

if __name__== "__main__":

  start = time.time()
  ans = solve()
  print "**************"
  stop = time.time()
  print ans
  print 'runtime: ' + str(stop-start) + ' sec.'
  

  
