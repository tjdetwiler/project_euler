

def get_digit_count(num):
    digit_count = -1
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
    return digit_count



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



def main():
    max_val = int(1e5)
    X = []
    for i in range(1,max_val):
        if i % 100000 == 0:
            print i
        stri = str(i)
        leni = len(stri)
         
        seti = set(stri)

        if stri[leni-1] == '0':
            continue

        jj = ((9-2*leni)/2)+1
        jmin = int(10**(jj-1))
        jmax = int(10**jj)

        for j in range(jmin,jmax):
            strj = str(j)
            setj = set(strj)
            if seti.intersection(setj):
                continue

            k = i * j
            strk = str(k)
            v = stri+strj+strk
            if len(v) != 9 or '0' in v:
                continue

            x = set(v)
            if len(x) == 9:
                h = int(k)
                if h not in X:
                    print (i,j,k)
                    X.append(h)
    print "****************"
    print sum(X)        
    

if __name__ == "__main__":
    main()
