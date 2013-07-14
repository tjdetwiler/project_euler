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


def main():
    
    n = 3
    count = 0
    prev_n_divisor_count =  len(list(divisorGen(2)))
    while n < 10000000:
        if n % 10000 == 0:
            print n
        n_divisor_count = len(list(divisorGen(n)))
        if n_divisor_count == prev_n_divisor_count:
            count +=1  
        n += 1
        prev_n_divisor_count = n_divisor_count
    return count
if __name__  == "__main__":
    result = main()
    print "**************"
    print result

