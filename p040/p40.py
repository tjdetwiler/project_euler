
def main():

    char_count = 0
    ds = [10**i for i in range(0,7)]
    m = 0
    X = []
    i = 1
    while True:
        istr = str(i)
        for c in istr:
            char_count += 1
            if char_count in ds:
                X.append(int(c))
                m += 1
                print "d_"+str(m) + " = " + c
                if m == len(ds): 
                    val = 1
                    for x in X:
                        val *= x
                    return val
        i += 1
    

if __name__ == "__main__":
    val = main()
    print "***************"
    print val
