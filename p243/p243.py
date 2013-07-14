

class PrimeGen(object):

    def __init__(self):
        self.current_prime = 2

    def prime_factors(self,n):
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

    def get_next_prime(self):
        num_factors = 2
        while num_factors != 1:
            self.current_prime +=1
            num_factors = len(self.prime_factors(self.current_prime))
        return self.current_prime
   


def main():
    prime_gen = PrimeGen()
    thresh = float(15499)/float(94744)
    P = [2]
    d = 0

    next_prime = prime_gen.get_next_prime()
    base = 2
    totient_base = (1-1./2)

    c = 0
    while True:
        for i in range(1,next_prime):
            if c % 1000 == 0:
                print c
            val = base*i
            totient = val*totient_base
            res = float(totient)/float(val-1)
            if res < thresh:
                return val
                print "*****"
                print val
            # print(val,totient,res)
            c+= 1
            # if c == 20:
            #     return
                                  
        P.append(next_prime)
        base *= next_prime
        totient_base *= (1-1./next_prime)
        next_prime = prime_gen.get_next_prime()
        # print "next prime: " + str(next_prime) 
    
    

if __name__== "__main__":
  result = main()
  print "***************"
  print result
