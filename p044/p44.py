import numpy as np

def get_pents(max_val_count):
    count = 0
    k = 1
    P =[]
    while len(P) < max_val_count:
       pn = k*(3.*k-1.)*0.5
       P.append(pn)
       k += 1
    return P

def is_int(x):
    eps = 1e-4
    if abs(x - int(x)) < eps:
        return 1
    return 0
    

def is_pentagonal(x):
    y = (np.sqrt(24.*x+1.)+1.)/6.
    return is_int(y)


def solve():
    max_val_count = 4000
    P = get_pents(max_val_count)
    min_D = float('inf')
    min_pair = None
    for i in range(0,len(P)):
        if i % 100 == 0:
            print i
        for j in range(i+1,len(P)):
            Ad = P[i] + P[j]
            if not is_pentagonal(Ad):
                continue
            Dd = P[j] - P[i]
            if not is_pentagonal(Dd):
                continue
            if Dd < min_D:
                min_D = Dd
                min_pair = (P[i],P[j])
               
    print min_pair
    return min_D
            
                
            



if __name__  == "__main__":
    min_v = solve()
    print "******************"
    print min_v
