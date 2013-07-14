import numpy as np
import mpmath


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

def add_last_digits(fn1,fn2):
    fn = [0]*9
    carry = 0
    for i in range(9-1,-1,-1):
        val = fn1[i] + fn2[i] + carry
        fn[i] = val % 10
        carry = val/10
    return fn
    
def first_digits_are_pandigital(val):
    val = mpmath.nstr(val,n=10)
    val = val.split('e')
    val = val[0]
    val = val.split('.')
    val = val[0]+val[1]
    val = val[:9]
    if len(set(val)) == 9 and '0' not in val:
        return 1
    return 0

def last_digits_are_pandigital(fn):
    if len(set(fn)) == 9 and 0 not in fn:
        return 1
    return 0


def solve():
    # mpmath.mp = 100
    fn1 = [0]*9
    fn2 = [0]*9
    fn1[8] = 1
    fn2[8] = 1
    k = 3
    vn1 = mpmath.mpf(1.000000000e0)
    vn2 = mpmath.mpf(1.000000000e0)

    while True:
        # if k % 1000 == 0:
        #     print k

        fn = add_last_digits(fn1,fn2)
        vn = vn1+vn2
        if last_digits_are_pandigital(fn):
            if first_digits_are_pandigital(vn):
                mpmath.nprint(vn,n=10)
                return k
      
        vn2 = vn1
        vn1 = vn

        fn2 = fn1
        fn1 = fn
        k += 1
        


if __name__ == "__main__":
    ans = solve()
    print "*****************"
    print ans

