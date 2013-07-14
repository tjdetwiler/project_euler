

def find_max(X):
    #argument X is is a dict()
    max_val = 0
    for k in X:
        v = X[k]
        if v > max_val:
            max_val = v
            max_val_key = k
    return (max_val_key,max_val)    


def main():
    pmax = 2000
    X = dict()
    for a in range(1,pmax):
        a_sq =  a**2
        for b in range(1,pmax):
            b_sq = b**2
            c = (a_sq+b_sq)**.5
            if round(c) != c:
                continue
            else:
                p = int(a + b + c)
                if p > 1000:
                    continue
                if p in X:
                    X[p] += 1
                else:
                    X[p] = 1
    print "*******************"
    (k,v) = find_max(X)
    print "P = " + str(k)




if __name__ == "__main__":
    main()
