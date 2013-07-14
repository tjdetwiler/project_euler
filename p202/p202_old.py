
import itertools

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



def factorGenerator(val):
  pfactors = prime_factors(val)
  pfactors.sort()
  factor_list = []
  for key,group in itertools.groupby(pfactors):
      factor_list.append( (key,len(list(group)) ) )

  return factor_list

def divisorGen(n):
    if n == 1:
        yield 1
        return 
    factors = list(factorGenerator(n))
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


def mobius(val):
    primes = prime_factors(val)
    print (val,primes)
    if len(list(set(primes))) == len(primes):
        #is square free
        if len(primes) % 2 == 0:
            #even number of square free prime factors
            return 1
        else:
            return -1
    else:
        return 0

def P(n):
    p = ((n+2)/2) - ((n+2)/3)
    # print p
    return p

def D(n):
    sum  = 0 
    pn = P(n)
    divisors = list(divisorGen(n))
    for d in divisors:
        pnd = P(n/d)
        print "P(n/d) = " + str(pnd) + " n,d = " + str((n,d)) 
        sum += mobius(d)*pnd
    # print "D(n) = " + str(sum)
    return pn - sum


def F(n):
    pn = P(n)
    dn = D(n)
    print "P(n) = " + str(pn)
    print "D(n) = " + str(dn)
    return ( pn - dn )

# def F(n):
#     sum  = 0 
#     divisors = list(divisorGen(n))
#     for d in divisors:
#         pnd = P(n/d)
#         print "P(n/d) = " + str(pnd) + " n,d = " + str((n,d)) 
#         sum += mobius(d)*pnd 
#         # if d != 1 and d != n:
#         #     sum -= F(d)
#     # print "D(n) = " + str(sum)
#     return sum

def main():
    orbit_len = 12
    orbit_len = 1000002
    # orbit_len = 88200           
    # orbit_len = 100
    n = orbit_len/2
    primes = prime_factors(n)
    divisors = list(divisorGen(n))
    print "prime factors of n = " + str(primes)
    print "divisors of n = " + str(divisors)

    fn = F(n)
    print "*********"
    print "F(n) = " + str(fn)
    



if __name__ == "__main__":
    main()
