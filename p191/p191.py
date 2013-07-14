from scipy.misc import comb


def get_unacceptable_late_day_arrangements(n):
    s = 0
    for k in range(2,n+1): 
        s += comb(n,k)*(2**(n-k))
    return s

def get_unacceptable_absent_day_arrangements(n):
    s = 01
    for k in range(2,n+1): 
        s += comb(n,k)*(2**(n-k))
    return s
    

def solve():

    for n in range(4,5):
        total_possibilities = 3**n    
        c = 0
        u = get_unacceptable_late_day_arrangements(n)
        print(total_possibilities,u)
         
        


if __name__== "__main__":
    ans = solve()
    print "****************"
    print ans
