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

def rad(n):
    R = 1
    primes = set(prime_factors(n) )
    for p in primes:
        R *= p
    return R

def solve():
    max_val =100000
    X = []
    for n in range(1,max_val+1):
        X.append((n,rad(n)))
        
    X.sort(key = lambda tup:tup[1])

    return X[10000-1][0]


if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans
