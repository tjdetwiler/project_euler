

def gk(k):
    return k*(3*k-1)/2

def main():
    max_val = 100
    P = [1]
    n = 1
    while True:
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
        if p >= 2000000:
            if p % 1000000 == 0:
                return n
        P.append(p)
        n += 1 

if __name__== "__main__":
    result = main()
    print "**************"
    print result
