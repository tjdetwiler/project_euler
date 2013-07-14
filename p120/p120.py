import numpy as np
import sympy

def rmax(a):
    R = [2]
    for n in range(1,2*a+1):
        r = (2*n*a) % (a**2)
        R.append(r)
    return max(R)

def solve():
    s = 0
    for a in range(3,1000+1):
        s += rmax(a)
    return s




if __name__ == "__main__":
    ans = solve()
    print "*****************"
    print ans


