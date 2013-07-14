import gc

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


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

def main():
    # note: got lucky and never checked 8 or 9 digit numbers
    #       7 will get you the solution
    digits = [1,2,3,4,5,6,7]
    print "getting primes..."
    primes = get_primes(10000000)
    P = []
    for p in primes:
        if p <= 7654321 and p >= 1234567:
            P.append(p)
    primes = []
    gc.collect()
    print "calculating permutations..."
    perms = all_perms(digits)
    print "checking permutations for primes..."
    R = []
    for p in perms:
        if p[6] % 2 == 0:
            continue
        val = digits_to_num(p)
        if val in P:
            R.append(val)
    print "******************"
    print max(R)

if __name__ == "__main__":
    main()



