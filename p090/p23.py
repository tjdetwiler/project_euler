import sys
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


def find_abundant_numbers():
   start_val = 2
   stop_val = 28124

   abundant_sums = []
   for i in range(start_val,stop_val):

       divisors = list(divisorGen(i))
       divisors = divisors[0:len(divisors)-1]

       divisor_sum = sum(divisors)

       if divisor_sum > i:
            abundant_sums.append(i)
   return abundant_sums


def find_non_abundant_sum_nums(ab_nums):

    max_val = 29000
    X = []
    Y = range(0,max_val)
    for i in range(0,len(ab_nums)):
        for j in range(i,len(ab_nums)):
            z = ab_nums[i] + ab_nums[j]
            if z < len(Y):
              Y[z] = 0


    YY = []
    for i in Y:
        if i != 0:
            YY.append(i)

    return YY

if __name__ == "__main__":

  ab_nums = find_abundant_numbers()

  Y = find_non_abundant_sum_nums(ab_nums)

  print sum(Y)
