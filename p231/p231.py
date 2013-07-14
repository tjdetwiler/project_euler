import sys


def product(val):
    s = 1;
    for i in range(0,len(val)):
        s = s * val[i];
    return s;
  

def test():
  for i in range(5,1,-1):
    print i 

def simplify(num,den):
   for i in range(0,len(num)):
        print 'i=' + str(i)
        for j in range(len(den)-1,-1,-1):
            print 'j=' + str(j)
            print 'testing ' + str(num[i]) + " / " + str(den[j]) 
            if num[i] % den[j] == 0:
                print 'removing ' + str(den[j])
                num[i] = num[i]/den[j]
                den.remove(den[j]);

                print 'i= ' + str(i)
                print 'num: ' + str(num)
                print 'den: ' + str(den)
                print '**********************'

                if len(den) == 0:
                    # print 'length den = 0'
                    return (num,[],0)
                else:
                    return (num,[],1)



def do_simplify(n,k):
    r = 1
    while r:
        (simp_n,simp_k,r) = simplify(n,k)
    return (simp_n,simp_k);
                
                
def get_numerator_list(n,k):
   if n-k < k:
     return range(k+1,n+1)
   else:
     return range(n-k+1,n+1)
   


def get_denominator_list(n,k):
   if n-k < k:
     return range(1,n-k+1)
   else:
     return range(1,k+1)
   




def get_prime_factorization_of_biomial_coeff(n,k):
    num_list = get_numerator_list(n,k)
    den_list = get_denominator_list(n,k)


if __name__ == "__main__":

    n = int(sys.argv[1])
    k = int(sys.argv[2])
    print 'getting list of denominators'
    den_list = get_denominator_list(n,k);
    # print den_list
    print 'getting list of numerators'
    num_list = get_numerator_list(n,k);
    # print num_list

    print 'simplifying...'
    (x,y) = do_simplify(num_list,den_list)
    print '(x,y):'
    # print x 
    # print y
    print sum(x)
    print product(x) 

    # prime_factors = get_prime_factorization_of_biomial_coeff(n,k);



