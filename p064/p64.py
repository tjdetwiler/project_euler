import numpy as np


def equals_int(f,i):
    epsilon = .001
    if abs(float(f) - float(i)) < epsilon:
        return 1
    return 0


def expansion_period(S):
        m = 0
        d = 1
        a0 = int(np.sqrt(S))
        a = int(a0)
        A = []
        k = 1
        while True:
            m = d*a-m
            d = (float(S) - m**2)/d
            a = int((a0 + m)/d)  
            if int(d) == 1:
                return k
            k += 1



def main():
    max_val = 10000
    count = 0
    for n in range(2,max_val+1):
        sq = np.sqrt(n)
        if equals_int(sq,int(sq)):
            continue
        c = expansion_period(n)
        if c % 2 == 1:
            count +=1 
    return count

if __name__== "__main__":
    result = main()
    print "*****************"
    print result
