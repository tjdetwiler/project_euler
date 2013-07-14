
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


def main():
    max_sq_val = 100000
    max_prime_val = 100000
    mv = 100000
    sqss = [2*(x**2) for x in range(0,max_sq_val+1)]
    sqs = []
    for s in sqss:
        if s < mv:
            sqs.append(s)

    sqss = []
    primes = [1]+get_primes(max_prime_val)
    z = [x for x in range(0,mv+1)]
    maxz = len(z)

    for i in range(0,len(z)):
        if z[i] % 2 == 0:
            z[i] = 0
        

    for i in range(0,len(primes)):
        p = primes[i]
        for j in range(0,len(sqs)):
            t = p + sqs[j]
            if t < maxz:
                z[t] = 0
     
    Z = list(set(z))
    Z.sort()
    print "********************"
    print Z[1]


if __name__  == "__main__":
    main()
