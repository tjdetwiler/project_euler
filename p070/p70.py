
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





# The trick here to to realize that the minimum ratios accur when values
# of n are used which are composed of only 2 unique primes
def solve1():
    max_prime = int(100000)
    primes = get_primes(max_prime)
    min_ratio = float('inf')
    min_n = 0
    for i in range(0,len(primes)):

        if i % 200 == 0:
            print(i,len(primes)) 
        for j in range(i+1,len(primes)):
            n = primes[i]*primes[j]
            if n > int(1e7):
                break 
            phi = n
            digits = get_digits(phi)
            phi *= (1 - 1.0/primes[i]) 
            phi *= (1 - 1.0/primes[j]) 

            totient_digits = get_digits(int(phi))
            digits.sort()
            totient_digits.sort()
            if digits == totient_digits:
                ratio = float(n)/float(phi)
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_n = n
                    # print (min_ratio,min_n)
    return min_n
    


if __name__== "__main__":
  n = 8319823
  ans = has_totient_permutation(n)
  # ans = solve2()
  print "***************"
  print ans
