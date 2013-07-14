import numpy as np


# extremely easy, u_n +u_n+1 turned out to be 
# basically stationary...
 
def fx(x):
    d = 1e-9
    y = 30.403243784 - x**2.
    z = np.floor(2**y)*d    
    return z

def solve():
    np.set_printoptions(precision=16)
    n = 0
    u = -1
    s = 0
    max_val = 100001
    while n <= max_val:
        u = fx(u)
        n += 1
        if n == max_val-1:
            s += u
        if n == max_val:
            s += u
    return s

        
                 
               
             

if __name__ == "__main__":
    ans = solve()
    print "***********"
    print ans
