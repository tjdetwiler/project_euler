import sys

ZERO_5 = 0
ONE_5 = 1
TWO_5 = 32
THREE_5 = 243
FOUR_5 = 1024
FIVE_5 = 3125
SIX_5 = 7776
SEVEN_5 = 16807
EIGHT_5 = 32768
NINE_5 = 59049

POWERS = [ ZERO_5,ONE_5,TWO_5,THREE_5,FOUR_5,FIVE_5,\
           SIX_5,SEVEN_5,EIGHT_5,NINE_5 ]



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

def get_fifth_power_of_digits_sum(digits):
    sum = 0
    for digit in digits:
        sum += POWERS[digit]
    return sum

def main():
    max_val = 500000
    X = []
    for i in range(10,max_val+1):
        digits = get_digits(i)
        fifth_pow_sum = get_fifth_power_of_digits_sum(digits)
        if fifth_pow_sum == i:
            X.append(i)   
    print X
    print "*****************"
    print sum(X)
     

if __name__ == "__main__":
    main()

