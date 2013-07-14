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

def totient(n):
    P = list(set(prime_factors(n)))
    phi = n
    for p in P:
        phi *= (1 - 1.0/p)
    return int(phi)


def main():
    S = 0
    max_val = 1000000
    for d in range(2,max_val +1):
        if d % 100000 == 0:
            print d
        x = totient(d)
        S += x
    print S
 
    

if __name__== "__main__":
  result = main()
  print "***************"
