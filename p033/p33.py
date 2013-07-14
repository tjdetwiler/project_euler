

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


def get_digits(num):
    digit_count = 2
    digits = []
    t = num
    for i in [1,0]:
        p = 10**i
        r = t/p
        digits.append(r)
        t = t - r*p
    return digits


def find_fractions():
    X = []
    for i in range(10,99):
        numerator_digits = get_digits(i)
        for j in range(i+1,100):
            denominator_digits = get_digits(j)
            
            a = numerator_digits[1]
            b = denominator_digits[0]
            c = numerator_digits[0]
            d = denominator_digits[1]

            if d == 0:
                continue

            if a == b:
                val1 = float(i)/float(j)
                val2 = float(c)/float(d)
                if val1 == val2:
                    X.append((i,j))


    return X

def multiply_fractions(X):
    num = 1
    den = 1

    for (a,b) in X:
        num = num * a
        den = den * b

    return (num,den)

def remove_val(val,X):
    while val in X:
      i = X.index(val)
      del X[i]

def simplify_fraction(num,den):
    print "simplifying fraction..."
    num_factors = prime_factors(num)
    den_factors = prime_factors(den)

    num_factors_set = set(num_factors)

    for val in num_factors_set:
      while True:
        if val in den_factors and val in num_factors:
            i = den_factors.index(val)
            del den_factors[i]
            i = num_factors.index(val)
            del num_factors[i]
        else:
            break;
        
    return (num_factors,den_factors)
    

if __name__ == "__main__":
    X = find_fractions()
    print "fractions of interest:"
    print X
    (num,den) = multiply_fractions(X)
    print "multiplying fractions together..."
    print (num,den)
    (n,d) = simplify_fraction(num,den)

    val = 1
    for i in d:
        val = val*i
    
    print "simplified denominator:"
    print val
