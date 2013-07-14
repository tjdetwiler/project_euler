import itertools
import collections
import operator

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

def digits_to_num(digits):
    val = 0 
    j = 0
    for i in range(len(digits)-1,-1,-1):
        val += (10**i)*digits[j]
        j += 1
    return val

def get_digits(num):
    digit_count = 0;
    if num < 10:
        digit_count = 1
    elif num < 100:
        digit_count = 2
    elif num < 1000:
        digit_count = 3
    elif num < 10000:
        digit_count = 4
    elif num < 100000:
        digit_count = 5
    elif num < 1000000:
        digit_count = 6
    elif num < 10000000:
        digit_count = 7
    elif num < 100000000:
        digit_count = 8
    elif num < 1000000000:
        digit_count = 9
    else:
        rem = 1
        digit_count = 10
        val = (10**digit_count)
        rem = num/val
        while rem != 0:
            digit_count += 1
            val = (10**digit_count)
            rem = num/val
        

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(int(r))
        t = t - r*p
    return digits


def get_primes_between(min_val,max_val):
    primes = [] 
    p = get_primes(max_val)
    for i in range(0,len(p)):
        if p[i] >= min_val and p[i] < max_val:
            primes.append(p[i])
    return primes

def get_replacable_digits(combination,digit_count):
    rd = []
    for i in range(0,digit_count):
        if i not in combination:
            rd.append(i)
    return rd
        
def solve():
    family_len = 8
    digit_count = 4
    min_prime = float('inf')
    min_vals = []
    while True:
        print 'digit count = ' + str(digit_count)
        max_val = (10**digit_count)
        min_val = (10**(digit_count-1))
        primes = get_primes_between(min_val,max_val)
        for c in range(1,digit_count):
            combs = itertools.combinations(xrange(0,digit_count),r = c)        
            for comb in combs:

                replacable_digits = get_replacable_digits(comb,digit_count) 
                vals = []
                vals_dict = {}                
                for prime in primes:
                    prime_digits = get_digits(prime) 
                    off_digits = operator.itemgetter(*replacable_digits)(prime_digits)
                    if type(off_digits) is int:
                        off_digits = [off_digits]
                    else:
                        off_digits = list(off_digits)

                    if len(set(off_digits)) != 1:
                        continue
                    off_digit = off_digits[0]
                    comb_digits = operator.itemgetter(*comb)(prime_digits)
                    if type(comb_digits) is int:
                        comb_digits = [comb_digits]
                    else:
                        comb_digits = list(comb_digits)
                    comb_val = digits_to_num(comb_digits)

                    if comb_val in vals_dict:
                        vals_dict[comb_val].append(prime)                    
                    else:
                        vals_dict[comb_val] = [prime]

                for comb_val in vals_dict:
                    if len(vals_dict[comb_val]) == family_len:
                        prmes = vals_dict[comb_val]
                        m = min(prmes)
                        if m < min_prime:
                            min_prime = m
                            min_combo = comb_val
                            min_vals = prmes
             

        if min_vals:
            return min_prime
        digit_count +=1
        



if __name__  == "__main__":
    ans = solve()
    print "*********************"
    print ans




