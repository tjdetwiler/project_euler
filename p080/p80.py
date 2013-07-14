
#http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Digit-by-digit_calculation

def digits_to_num(digits):
    val = 0 
    j = 0
    for i in range(len(digits)-1,-1,-1):
        val += (10**i)*digits[j]
        j += 1
    return val


def get_x_and_y(p,c):
    x = 0
    y = -1
    while y <= c:
        x += 1
        y = x*(20*p+x) 
    x -= 1
    y = x*(20*p+x) 
    return (x,y)

#known by problem statement 1 <= S < 100 (100 is rational)
def expand_sqrt(S):
    digits = []
    digit_count = 100
    p = 0
    c = S
    while len(digits) < digit_count:
        (x,y) = get_x_and_y(p,c)
        digits.append(x)
        p = digits_to_num(digits)
        c = (c - y)*100
        if c == 0:
            return digits
    return digits
    



def main ():
    S = 0
    for n in range(1,100):
        digits = expand_sqrt(n)
        if len(digits) == 100:
            S += sum(digits)
    print "*************"
    print S



if __name__ == "__main__":
    main()
