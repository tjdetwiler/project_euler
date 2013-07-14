import itertools
import collections
import operator
import copy

six_digit_primes = []


def get_primes_list(primes):
    max_digit_count = len(get_digits(primes[len(primes)-1]))
    pr = primes
    primes_list = [0]
    for i in range(0,max_digit_count):
        primes_list.append([])
    for i in range(0,max_digit_count):
        index = i +1
        min_val = 10**i
        max_val = (10**(i+1))-1
        for p in pr:
            if p >= min_val:
                if p <= max_val:
                    primes_list[index].append(p)
                else:
                    break
    return primes_list

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


def is_prime(a):
    return all(a % i for i in xrange(2, a))

mem = {}

def can_concat(a,b,primes_list):
    global mem

    key = (min(a,b),max(a,b))
    if key in mem:
        return mem[key]


    A = get_digits(a)
    B = get_digits(b)
    C = A+B
    val = digits_to_num(C)
    index = len(C)
    if index < len(primes_list):
        primes = primes_list[index]
        max_prime = primes[len(primes)-1]
    else:
        max_prime = -1
    if val > max_prime:
        if not is_prime(val):
            mem[key] = 0
            return 0
    else:
        if val not in primes:
            mem[key] = 0
            return 0

    C = B+A
    val = digits_to_num(C)

    if val > max_prime:
        if not is_prime(val):
            mem[key] = 0
            return 0
    else:
        if val not in primes:
            mem[key] = 0
            return 0

    mem[key] = 1
    return 1



def can_add_to_set(prime,primes_list,Set):
    a = prime
    for b in Set:        
        if not can_concat(a,b,primes_list):
            return 0
    return 1
        


        
def solve():
    global six_digit_primes
    max_digit_count = 4
    max_prime = 10**(max_digit_count)-1
    print 'finding primes'
    C = []

    primes = get_primes(max_prime)
    # primes_list = get_primes_list(primes)
    for j in range(0,len(primes)):
        # if j % 1000 == 0:
        #     print (j,len(primes))
        p = primes[j]
        digits = get_digits(p)

        for i in range(1,len(digits)):
            a = digits_to_num(digits[:i])
            if a not in primes:
                continue
            b = digits_to_num(digits[i:])
            if b not in primes:
                continue
            C.append((a,b))
            
    C.sort(key = lambda x:x[0])
    D = []
    for c in C:
       c_flip = (c[1],c[0])
       if c_flip in C:
           if c not in D and c_flip not in D:
               D.append(c)

    for d in D:
        print d
    return len(D)
    



if __name__  == "__main__":
    ans = solve()
    print "*********************"
    print ans




