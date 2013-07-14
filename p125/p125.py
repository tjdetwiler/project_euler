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

def is_palindrome(val):
    digits = get_digits(val)
    if digits == digits[::-1]:
        return 1
    return 0

def solve():
    count = 0
    A = []
    max_val = int(1e8)
    sqs = [ x**2 for x in range(1,int(np.sqrt(max_val))+1)]
    SS = 0
    for i in range(0,len(sqs)-1):
        # if i % 1000 == 0:
        #     print i
        j = i
        s = sqs[j]
        j += 1
        s += sqs[j]
        
        while s < max_val:
            if is_palindrome(s):
                if s not in A:
                    A.append(s)
                    SS += s
            j += 1
            if j == len(sqs):
                break
            s += sqs[j]

    A.sort()
    print len(A)
    print len(set(A))
    return SS

if __name__ == "__main__":
    ans = solve()
    print "***********"
    print ans
