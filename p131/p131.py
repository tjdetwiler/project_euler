import numpy as np
import time
c
def get_primes(max_val):
    vals = list(range(0,max_val+1))
    vals[1] = 0;

    for i in range(2,len(vals)/2 + 2):
      v = vals[i]
      # if v != 0 , then v is prime
      if v == 0:
          continue
      m = 2
      r = m*v

      while r <= max_val:
          vals[r] = 0
          m += 1
          r = m*v
    X = []
    for v in vals:
        if v != 0:
            X.append(v)
    return X


def is_positive_int(val):
    if val < 0:
        return 0
    eps = 1e-6
    return (np.abs(val-int(val)) < eps)

    

# found pattern that n is always a power of 3 of some integer x
# and that r is n + x**2 for valid primes 
def solve():
    count = 0
    max_val = int(1e6)
    P = list(get_primes(max_val))
    x = 1
    while x < 580:
        x2 = x**2
        n = x**3
        n2 = n**2
        n3 = n**3
        r = n+x2
        r3 = r**3
        p = (r3-n3)/n2
        if p in P:
            count += 1
        x += 1

    return count


        
        
    


if __name__ == "__main__":
    start = time.time()
    ans = solve()
    end = time.time()
    print "***********"
    print ans
    print "runtime: " + str(end-start) + "seconds"
    

