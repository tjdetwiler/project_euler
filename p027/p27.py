

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



def test():
    #check method with example given in problem
    print "finding primes..."
    p = get_primes(20000)
    max_p = max(p) 
    n = 0
    a = -79
    b = 1601
    consec_prime_count = 0
    y = n**2 + a*n + b
    print y
    while y in p :
        print y
        consec_prime_count += 1
        n += 1
        y = n**2 + a*n + b
        # y += 2*n + 1 + a
        if y > max_p:
            print "warning y = " + str(y)
            print "max prime val = " + str(max_p)
    print "*****************"
    print consec_prime_count


if __name__ == "__main__":
    print "finding primes..."
    p = get_primes(20000)
    max_p = max(p)
    # print len(p)
    # exit(0)
    max_consec_prime_count = 0
    print "starting search..."

    for a in range(-999,1):
        if a % 100 == 0:
            print "a = " + str(a)
        for b in range(-999,1000):
            n = 0
            consec_prime_count = 0
            y = n**2 + a*n + b
            while y>0 and y in p :
                consec_prime_count += 1
                n += 1
                y = n**2 + a*n + b
                # y += 2*n + 1 + a
                if y > max_p:
                    print "warning y = " + str(y)
                    print "max prime val = " + str(max_p)
            if consec_prime_count > max_consec_prime_count:
                max_consec_prime_count = consec_prime_count
                amax = a
                bmax = b

    print "*************************"
    print "max consecutive prime count: " + str(max_consec_prime_count)
    print (amax,bmax)
    print amax*bmax
            
