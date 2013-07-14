

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
        return []

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(r)
        t = t - r*p
    return digits

def is_nine_digit_pandigital(num):
    if num >= int(1e8) and num < int(1e9):
        digits = get_digits(num)
        if len(digits) == len(set(digits)):
            if 0 not in digits:
                return 1
    return 0

def main():
    max_val = int(1e5)
    X = []
    for num in range(1,max_val):
        x = 0
        xstr = ""
        j = 1
        while True:
            x = num*j
            xstr += str(x)

            if len(xstr) > 9:
                break
            if len(xstr) == 9:
                x = int(xstr)
                if is_nine_digit_pandigital(x):
                    X.append(x)
            j += 1 
    return X

if __name__== "__main__":
    X = main()
    print X 
    print "**********************"
    if X:
        print max(X)
