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
             


def solve():
    goal = 1000
    num = 178000
    max_count = 0
    while True:
        divisors = list(divisorGen(num))
        mn_same = 0
        count = 0
        pairs = []
        for k in divisors:
            for m in divisors: 
                for n in divisors:  
                    z = k*m*n
                    if z == num:
                        x = k*m*(n+m)
                        y = k*n*(n+m)
                        pair  =(min(x,y),max(x,y))
                        if pair not in pairs:
                            pairs.append((min(x,y),max(x,y)))
                            count += 1

        if count >= goal:
            return num
        num += 2
           
                        
                    
    



if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans
