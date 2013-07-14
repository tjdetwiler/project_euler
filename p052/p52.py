
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
    else:
        return []

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(r)
        t = t - r*p
    return digits


def has_permuted_multiples(val,digits):
    digits.sort()
    # check multiples of 2,3,4,5,6 of val
    for i in range(2,7):
        valx = val*i
        perm_digits = get_digits(valx)
        perm_digits.sort()
        if not digits == perm_digits:
            return 0
    return 1


if __name__ == "__main__":
    max_test_val = 1000000
    for i in range(1,max_test_val+1):
        digits = get_digits(i)
        if has_permuted_multiples(i,digits):
            print "****************"
            print i
            exit(0)

    print "nothing found."

