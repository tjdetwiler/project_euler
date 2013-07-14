
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
    # print "n=" + str(n)
    if n == 1:
        yield 1
        return
    factors = list(factorGenerator(n))
    nfactors = len(factors)
    # print "nfactors = " + str(nfactors)
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


# def is_non_duplicate(x,y):
#     # print (x,y)
#     x_divs = set(list(divisorGen(x)))
#     y_divs = set(list(divisorGen(y)))
#     gcd = max(x_divs.intersection(y_divs))
#     if gcd == 1:
#         return 1
#     if x % 3 == 0 and y % 3 == 0:
#         a = x/3
#         b = y/3
#         if b%3 == 0:
#             return 0
#         a_divs = set(list(divisorGen(a)))
#         b_divs = set(list(divisorGen(b)))
#         gcd = max(a_divs.intersection(b_divs))
#         if gcd != 1:
#             return 0
#         else: 
#             return 1
#     return 0

def rwh_primes1(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]



def get_primes(max_val):
    vals = list(xrange(0,max_val+1))
    vals[1] = 0;

    for i in xrange(2,len(vals)/2 + 2):
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

def is_non_duplicate(x,y,n_divs):
    for d in n_divs:
        if x % d == 0 and y % d == 0:
            return 0
    return 1
    
         
def tt():
    c = 0
    i = 0
    while i < 6000000000:
        if i % 10000000 == 0:
            print i
        c +=1    
        i +=3


def main():
    bounces = 1000002/2 +1
    # bounces = 88200/2 +1
    bounces = (12017639147+1)/2 +1
    # bounces = 100/2
    n = bounces
    n_divs = list(divisorGen(n))[1:]
    n_divs.sort()
    print n_divs
    x =  n
    print 'found divs, count = ' + str(len(n_divs))

    while True:
        y = n - x 
        if x % 3 == y % 3:
            if x > y:
                print (x,y)
                # temp = y
                # y = x
                # x = temp
                break
             
        x -= 1
    c = 0
    print 'found '
    while x > y:
        if y % 1000000 == 0:
            print (x,y)
        if is_non_duplicate(x,y,n_divs):
            # print (x,y)
            c += 1
        # else:
            # print ".. " + str((x,y))
        x -= 3
        y += 3

    print "*******************"
    print 2*c


# def main():
#     bounces = 1000002/2 +1
#     # bounces = 12/2 + 1
#     # bounces = (12017639147+1)/2 +1
#     # bounces = (88200)/2 +1
#     n = bounces
#     n_divs = list(divisorGen(n))
#     n_primes = get_primes(n)
#     # print n_primes
#     print n_divs
#     c = 0
#     for x in xrange(1,n+1):
#         if x % 100000000 == 0:
#             print x
#         y = n - x
#         if x > y:
#             if x % 3 == y % 3:
#                 # if x > 0 and y > 0: 
#                     if is_non_duplicate(x,y,n_divs[1:]):
#                         # print (x,y)
#                         c += 1

#     print "*******************"
#     print 2*c


if __name__ == "__main__":
    main()
