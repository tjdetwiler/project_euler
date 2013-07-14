



def main():
    pb = [10**i for i in range(0,7)]
    maxval = 1000000
    X = []
    for i in range(1,maxval+1):
        if i in pb:
            print i
        x = str(i)
        xr = x[::-1]
        if not x == xr:
            continue
        b = "{0:b}".format(i)
        br = b[::-1]
        if not b == br:
            continue
        X.append(i)
    print "*******************"
    print sum(X)


if __name__ == "__main__":
    main()
