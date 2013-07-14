import sys
import numpy as np

def get_digits(num):
    digit_count = 0;
    if num < 10:
        digit_count = 1
    elif num < 100:
        digit_count = 2
    elif num < 1000:
        digit_count = 3
    elif num < 10000:
        digit_count = 4
    elif num < 100000:
        digit_count = 5
    elif num < 1000000:
        digit_count = 6
    elif num < 10000000:
        digit_count = 7
    elif num < 100000000:
        digit_count = 8
    elif num < 1000000000:
        digit_count = 9
    else:
        rem = 1
        digit_count = 10
        val = (10**digit_count)
        rem = num/val
        while rem != 0:
            digit_count += 1
            val = (10**digit_count)
            rem = num/val
        

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(int(r))
        t = t - r*p
    return digits


def get_figurate_numbers():
    min_val = 999
    max_val = 10000
    n = range(1,max_val+1)
    P = {}
    P[0] = [x*(x+1)/2 for x in n if x*(x+1)/2 < max_val and x*(x+1)/2 > min_val]
    P[1] = [x*x for x in n if x*x < max_val and x*x > min_val]
    P[2] = [x*(3*x-1)/2 for x in n if x*(3*x-1)/2 < max_val and x*(3*x-1)/2 > min_val]
    P[3] = [x*(2*x-1) for x in n if x*(2*x-1) < max_val and x*(2*x-1) > min_val]
    P[4] = [x*(5*x-3)/2 for x in n if x*(5*x-3)/2 < max_val and x*(5*x-3)/2 > min_val]
    P[5] = [x*(3*x-2) for x in n if x*(3*x-2) < max_val and x*(3*x-2) > min_val]
    return P


def is_cyclic(a,b):
    a_digits = get_digits(a)
    b_digits = get_digits(b)
    if a_digits[2:] == b_digits[:2]:
        return 1
    return 0

def can_traverse(M,path):

    rows_touched = [r for (v,r) in path]
    parent = path[len(path)-1]

    if parent in M:
        children = M[parent]
    else:
        return 0

    for (v,r) in children:
        if len(path) == 6:
            if (v,r) == path[0]:
                return 1
        else: 
            if r not in rows_touched:
                path.append((v,r))
                if can_traverse(M,path):
                    return 1
                else:
                    path.pop()
    return 0     
            



def max_traveral_depth(M):
    c = 0
    for k in M:
        c += 1
        path = [k] 
        if can_traverse(M,path):
            return path
    
    return []

    

def solve():
    P = get_figurate_numbers()
    M = {}
    A = []

    for i in range(0,len(P)):
        for m in range(0,len(P[i])):
            a = P[i][m]
            for j in range(i+1,len(P)):
                for n in range(0,len(P[j])):
                    b = P[j][n]
                    if is_cyclic(a,b):
                        if (a,i) in M:
                            M[(a,i)].append((b,j))
                        else:
                            M[(a,i)] = [(b,j)]
                         
                    if is_cyclic(b,a):
                        if (b,j) in M:
                            M[(b,j)].append((a,i))
                        else:
                            M[(b,j)] = [(a,i)]

    path = max_traveral_depth(M)
     

    print path
       
    return sum([v for (v,r) in path])
        



if __name__== "__main__":

  ans = solve()
  print "**************"
  print ans
  

  

