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



def solve():
    max_val = 10**8
    # max_val = 30
    print 'getting primes'
    primes = get_primes(max_val)
    print 'computing'
    # (prime,index of primes it was last multiplied with)
    P = [(primes[0],0)]
    mem = [primes[0]*primes[0]] 
    n = 1
    count  = 1
    nv = 0
    nv_step = 1000000
    while True:
        Pnew = []
        N = {}

        for key in P:
            (prime,mult_index) = key
            if mult_index + 1 < len(primes):
                N[prime*primes[mult_index+1]] = (prime,mult_index+1)
            else:
                print "going out of bounds"
                print (prime,mult_index)
                exit(0)

        S = list(N)
        S.sort()
        # print 'S = ' + str(S)         
        for i in range(0,len(S)):
            pn = primes[n]*primes[n]
            s = S[i]
            if s > nv:
                print s
                nv += nv_step
            if pn < s:
                if pn < max_val:
                   count += 1
                   Pnew.append((primes[n],n))
                   mem.append(pn)
                   # print pn
                   n += 1
                   for j in range(i,len(S)):
                       s = S[j]
                       if s < max_val:
                           count += 1
                           mem.append(s)
                           # print s
                           Pnew.append(N[s])                                       
                           break

            elif s < max_val:
               count += 1
               # print s
               mem.append(s)
               Pnew.append(N[s])

        # print 'mem = ' + str(mem)
        
        if Pnew:
            # print 'P = ' + str(P)
            P = Pnew
        else:
            return count
        # print "^^^^^^^^^^^^^^^"



if __name__ == "__main__":
    ans = solve()
    print "***********"
    print ans
