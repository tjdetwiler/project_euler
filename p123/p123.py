import numpy as np
import sympy

# similar method used in problem 120

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


def r(pn):
    R = [2]
    for n in range(1,2*pn+1):
        r = (2*n*pn) % (pn**2)
        R.append(r)
    return max(R)

def solve():
    thresh = int(1e10)
    max_prime = int(1e5)
    k = 1
    while True:
        max_prime = int(1e5)+k*int(1e4)
        primes = get_primes(max_prime)
        for n in range(0,len(primes)):
            N = n + 1
            if N % 2 == 0:
                continue
            else:
                pn = primes[n]
                r = (2*N*pn) % (pn**2)
            if r > thresh:
                return N
        k += 1
        




if __name__ == "__main__":
    ans = solve()
    print "*****************"
    print ans


