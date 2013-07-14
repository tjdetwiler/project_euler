
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

def totient(n):
    P = list(set(prime_factors(n)))
    phi = n
    for p in P:
        phi *= (1 - 1.0/p)
    return int(phi)


def main():
    ratios = [0,0]
    max_val = 20
    for n in range(2,max_val+1):
        if n % 100000 == 0:
            print n
        phi = totient(n)
        print(n,phi)
        ratios.append(float(n)/float(phi))

    mx = 0.0
    mx_n = 0
    for i in range(0,len(ratios)):
        ratio = ratios[i]
        if ratio > mx:
            mx = ratio
            mx_n = i

    return mx_n
            
 
    

if __name__== "__main__":
  result = main()
  print "***************"
  print result
