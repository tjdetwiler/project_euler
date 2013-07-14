import numpy as np

def solve():
    # set to 
    power_of_ten = 100
    S = 0
    v = [1]*9
    # sum increasing numbers
    for i in range(0,power_of_ten):
        S += sum(v)
        v = np.cumsum(v)

    # sum decreasing numbers
    a = np.array([0]*9)
    b = np.array(range(1,10))
    for i in range(0,power_of_ten-1):
        S += sum(a+b)
        a = np.cumsum(a+b)
    return S



if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans








