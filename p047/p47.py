

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


def main():
    
    consecutive = 0
    num = 10
    while True:
        if num % 100j000 == 0:
            print num
        vals = set(prime_factors(num))
        if len(vals) == 4:
            consecutive += 1 
            if consecutive == 4:
                print [num-3,num-2,num-1,num]
        else:
            consecutive = 0 
        num  += 1


if __name__  == "__main__":
    main()
