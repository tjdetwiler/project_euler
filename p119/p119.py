import numpy as np


def digits_to_num(digits):
    val = 0 
    j = 0
    for i in range(len(digits)-1,-1,-1):
        val += (10**i)*digits[j]
        j += 1
    return val

def get_digits(num):
    digit_count = 0;
    if num < 10:
        digit_count = 1
    elif num < 100:
        digit_count = 2
    elif num < 1000:
        digit_count = 3
    elif num < 10000:
        digit_count = 4
    elif num < 100000:
        digit_count = 5
    elif num < 1000000:
        digit_count = 6
    elif num < 10000000:
        digit_count = 7
    elif num < 100000000:
        digit_count = 8
    elif num < 1000000000:
        digit_count = 9
    else:
        rem = 1
        digit_count = 10
        val = (10**digit_count)
        rem = num/val
        while rem != 0:
            digit_count += 1
            val = (10**digit_count)
            rem = num/val
        

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(int(r))
        t = t - r*p
    return digits



def solve():
    X = {}
    A = []
    for n in range(3,70):
        for p in range(2,11):
            val = np.power(n,p)
            if val in X:
                X[val].append((n,p))
            else:
                X[val] = [(n,p)]
    Z = [k for k in X]
    Z.sort()
    for z in Z:
        for (n,p) in X[z]: 
            if sum(get_digits(z)) == n:
                A.append(z)
                if len(A) == 30:
                    return A[29]
             
               
             

if __name__ == "__main__":
    ans = solve()
    print "***********"
    print ans
