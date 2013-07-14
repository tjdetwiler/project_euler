
# http://en.wikipedia.org/wiki/Pentagonal_number_theorem
# http://en.wikipedia.org/wiki/Partition_(number_theory)

def gk(k):
    return k*(3*k-1)/2

def main():
    max_val = 100
    P = [1]
    for n in range(1,max_val+1):
        i = 1
        g = gk(i)
        p = 0
        while g <= n:

            px = P[n-g]*int((-1)**(i-1))
            p += px

            if i ==0:
                i = 1
            elif i < 0:
                i = (-1*i) +1
            else: 
                i = -1*i    
            g = gk(i)

        P.append(p)

    # subtract 1 here because it includes the partition of 100 + 0     
    return P[max_val] - 1

if __name__== "__main__":
    result = main()
    print "**************"
    print result
