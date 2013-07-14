import numpy as np


def main():
     Pi = (1./4.)*np.array([0,1,1,1,1])
     Ci = (1./6.)*np.array([0,1,1,1,1,1,1])
     P = Pi
     C = Ci
     Pete_die_count = 9
     Colin_die_count = 6
     for i in range(0,Pete_die_count-1):
         P = np.convolve(P,Pi)
     for i in range(0,Colin_die_count-1):
         C = np.convolve(C,Ci)
    
     Pr = 0
     for i in range(0,len(C)):
         # print (sum(P[i+1:]),C[i])
         px = sum(P[i+1:])*C[i]
         # print px
         Pr += px
             
     return Pr
if __name__ == "__main__":
    result = main()
    print "**********"
    print result
