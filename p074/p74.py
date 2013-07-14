



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


def sum_of_factorial_of_digits(n):
    fact = [1,1,2,6,24,120,720,5040,40320,362880]
    digits = get_digits(n)
    S = 0
    for d in digits:
        S += fact[d]
    return S


def number_non_repeating_terms(n,mem):
    if n in mem:
        return mem[n]
    orig_value = n
    count = 0
    past = []
    while True:
        past.append(n)
        n = sum_of_factorial_of_digits(n)
        if n in mem:
            chain_length = len(past)
            remaining_count = mem[n]
            for i in range(0,len(past)):
                mem[past[i]] = remaining_count + chain_length-i
            return chain_length + mem[n]
        if n in past:
            chain_length = len(past)
            index = past.index(n)
            for i in range(0,past.index(n)+1):
                mem[past[i]] = chain_length-i
            return chain_length

        
def solve():
    max_val = 1000000
    mem = {}
    count = 0
    for n in range(1,max_val+1):
        if n %100000 == 0:
            print n
        val = number_non_repeating_terms(n,mem)
        if val == 60:
            count += 1
    return count
       


if __name__ == "__main__":
    ans = solve()
    print "**************"
    print ans
