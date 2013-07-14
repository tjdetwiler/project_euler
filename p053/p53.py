
def bin_coeff(n,k,factorials):
    val = factorials[n]/factorials[k]
    val = val/factorials[n-k]
    return val
    


def main():
    fac = 1 
    facts = []
    facts.append(1)
    thresh = 1000000
    count = 0
    for i in xrange(1,101):
        fac *= i
        facts.append(fac)

    for n in range(1,101):
     k = 1  
     while k <= n:  
        val = bin_coeff(n,k,facts)
        # print (n,k,val)
        if val> thresh:
            count += 1
        k += 1

            
    print 'done'
    return count



if __name__ == "__main__":
    count = main()
    print count
