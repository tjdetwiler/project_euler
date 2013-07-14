

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



def get_min_max_primes(min_val,max_val):
    all_primes = get_primes(max_val+1)
    primes = []
    for p in all_primes:
        if p >= min_val and p <= max_val:
            primes.append(p)
    return primes

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

def is_prime(val):
    f = prime_factors(val)
    if len(f) == 1 and f[0] == val:
        return 1
    return 0
        

def main():

    diag_num_count = 5
    prime_diag_count = 3
    ratio = float(prime_diag_count)/float(diag_num_count)

    loop_num = 2
    side_len = 3

    index = 9

    c = 0
    print "(index, side length, ratio)"
    while True:
      if c % 1000 == 0:
          print (index,side_len,ratio)
      c += 1
      side_len += 2      

      for i in range(0,4):
          index += side_len -1
          diag_num_count +=1
          if is_prime(index):
              prime_diag_count +=1
          ratio = float(prime_diag_count)/float(diag_num_count)

          if ratio < .1:
              print "****************"
              print side_len
              return
    

if __name__== "__main__":
    main()
