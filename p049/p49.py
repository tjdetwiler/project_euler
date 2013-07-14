

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



def main():
    all_primes = get_primes(10000)
    primes = []
    for p in all_primes:
        if p > 999 and p < 10000:
            primes.append(p)

    for i in range(0,len(primes)-2):
        a = primes[i]
        for j in range(i+1,len(primes)-2):
            b = primes[j]
            digits_a = get_digits(a)
            digits_b = get_digits(b)
            digits_a.sort()
            digits_b.sort()
            if digits_a == digits_b:
                diff_a = b - a
                val_c = b + diff_a
                if val_c in primes:
                    index_c = primes.index(val_c)
                    c = primes[index_c]
                    digits_c = get_digits(c)
                    digits_c.sort()
                    if digits_b == digits_c:
                        print (a,b,c)


    

if __name__ == "__main__":
    main()
