
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
    else:
        return []

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(r)
        t = t - r*p
    return digits


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


def is_prime_when_truncating_(digits,primes):
    for i in range(1,len(digits)):    
        trunc_digits = digits[i:]

        val = digits_to_num(trunc_digits)
        if not val in primes:
            return 0
        trunc_digits = digits[:i]
        val = digits_to_num(trunc_digits)
        if not val in primes:
            return 0
    return 1

def main():
    # ans: [23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397]

    primes = get_primes(750000)
    X = []
    c = 0
    for val in primes: 

       c += 1 
       if c % 500 == 0:     
           print c
           print "....   "  + str(val)
       digits = get_digits(val)
       if digits[0] == 1 or digits[len(digits)-1] == 0:
           continue
       if not is_prime_when_truncating_(digits,primes):
           continue

       X.append(val)
       if len(X) == 15:
           break

    print "*************"
    print "numbers found: " + str(len(X[4:]))
    print X[4:]
    print "sum: " + str(sum(X[4:]))
        


if __name__ == "__main__":
    main()
