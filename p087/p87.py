import numpy as np


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


def get_prime_squares(P,max_val):
    X = []
    i = 0
    pp = P[i]**2
    while pp < max_val:
            X.append(pp)
            i += 1
            pp = P[i]**2
    return X

def get_prime_cubes(P,max_val):
    X = []
    i = 0
    pp = P[i]**3
    while pp < max_val:
            X.append(pp)
            i += 1
            pp = P[i]**3
    return X

def get_prime_quartics(P,max_val):
    X = []
    i = 0
    pp = P[i]**4
    while pp < max_val:
            X.append(pp)
            i += 1
            pp = P[i]**4
    return X

def prime_factors(n):
    "Returns all the prime factors of a positive integer"
    factors = []
    d = 2
    while (n > 1):
        while (n%d==0):
            factors.append(d)
            n /= d
        d = d + 1
        if (d*d>n):
            if (n>1): factors.append(n);
            break;
    return factors


def main():
    # print prime_factors(6)
    max_val = 50000000
    print 'getting primes'
    # P = get_primes(int(np.ceil(np.sqrt(max_val))))
    P = get_primes(max_val)
    print 'getting subsets'
    sqs = get_prime_squares(P,max_val)
    cubes = get_prime_cubes(P,max_val)
    quars = get_prime_quartics(P,max_val)
    # print sqs
    # print cubes
    # print quars
    
    P = []
    print 'calculating...'
    for s in sqs:
        for c in cubes:
            for q in quars:
                sum = s + c + q
                if sum < max_val:
                       P.append(sum)
                else:
                   break
    count = len(set(P))
    return count



if __name__  == "__main__":
    X = main()
    print "*********************"
    print X




