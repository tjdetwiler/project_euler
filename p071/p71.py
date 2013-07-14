import numpy as np


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

def simplify_fraction(fraction):
    (num,den) = fraction
    num_primes = prime_factors(num)
    den_primes = prime_factors(den)
    a = set(num_primes)
    b = set(den_primes)
    while True:
        c = a.intersection(b)
        if c:
            for cc in c:
                num = num/cc
                den = den/cc
            num_primes = prime_factors(num)
            den_primes = prime_factors(den)
            a = set(num_primes)
            b = set(den_primes)

        else:
            return (num,den)
        

def main():
    
    dmax = 1000000
    thresh = float(3)/float(7)
    max_val = 0
   
    for d in range(1,dmax+1):
        n = int(np.ceil(thresh*d))
        val = 1 
        while True:
            val = float(n)/float(d)
            if val < thresh:
                if val > max_val:
                    max_num = n
                    max_den = d
                    max_val = val
                break
            n -= 1

    return (max_num,max_den)

if __name__ == "__main__":
    x = main()
    x = simplify_fraction(x)
    print "***********"
    print x[0]
