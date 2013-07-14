import numpy as np


def equals_int(f,i):
    epsilon = .001
    if abs(float(f) - float(i)) < epsilon:
        return 1
    return 0


class Pell(object):
    
    def __init__(self,S):
        self.m = 0
        self.d = 1
        self.a0 = int(np.sqrt(S))
        self.a = int(np.sqrt(S))
        self.S = S
        self.h = [0,1]
        self.k = [1,0]
        # print "(m,d,a) = " + str((self.m,self.d,self.a))

    def get_next_convergent_fraction(self):
        l = len(self.h)
        hn = self.a*self.h[l-1] + self.h[l-2]
        kn = self.a*self.k[l-1] + self.k[l-2]
        self.h.append(hn)
        self.k.append(kn)

        self.m = self.d*self.a-self.m
        self.d = (float(self.S) - self.m**2)/self.d
        self.a = int((self.a0 + self.m)/self.d)
        # print "(m,d,a) = " + str((self.m,self.d,self.a))

        return (hn,kn)



def main():
    max_val = 1000
    max_x = 0
    for D in range(2,max_val + 1):
        sqr = np.sqrt(D)
        if equals_int(sqr,int(sqr)):
            continue
        P = Pell(D)
        result = 0
        while not result:
            (x,y) = P.get_next_convergent_fraction()
            f = x**2 - D*y**2
            result = equals_int(f,1)
        if D == 661:
            print (D,x,y)
        if x > max_x:
            max_x = x
            max_D = D
    return max_D

if __name__== "__main__":
    result = main()
    print "*****************"
    print result
