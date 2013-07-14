import numpy as np


def greatest_horizontal_sum(mat):
    max_ending_here = 0
    max_so_far = 0
    j = 0
    for i in range(0,2000):
        max_ending_here = 0
        x = i
        y = j 
        while x < 2000 and y < 2000:
            next_val = mat[x,y] 
            max_ending_here = max(0,max_ending_here + next_val)
            max_so_far = max(max_so_far,max_ending_here)
            y += 1
    return max_so_far



def greatest_vertical_sum(mat):
    max_ending_here = 0
    max_so_far = 0
    i = 0
    for j in range(0,2000):
        max_ending_here = 0
        x = i
        y = j 
        while x < 2000 and y < 2000:
            next_val = mat[x,y] 
            max_ending_here = max(0,max_ending_here + next_val)
            max_so_far = max(max_so_far,max_ending_here)
            x += 1
    return max_so_far



def greatest_diagonal_sum(mat):
    max_ending_here = 0
    max_so_far = 0
    for i in range(0,2000):
        for j in range(0,2000):
            if i != 0 or j != 0:
                break;
            max_ending_here = 0
            x = i
            y = j 
            while x < 2000 and y < 2000:
                next_val = mat[x,y] 
                max_ending_here = max(0,max_ending_here + next_val)
                max_so_far = max(max_so_far,max_ending_here)
                x += 1
                y += 1 
    return max_so_far

def greatest_anti_diagonal_sum(mat):
    max_ending_here = 0
    max_so_far = 0
    for i in range(0,2000):
        for j in range(0,2000):
            if i != 1999 or j != 0:
                break;
            max_ending_here = 0
            x = i
            y = j 
            A = mat[i,j]
            while x < 2000 and y < 2000:
                next_val = mat[x,y] 
                max_ending_here = max(0,max_ending_here + next_val)
                max_so_far = max(max_so_far,max_ending_here)
                x -= 1
                y += 1 
    return max_so_far


def solve():
    print 'creating matrix'
    S = [0]
    for k in range(1,56):
        sk = ( (100003 - 200003*k + 300007*(k**3) ) % 1000000 ) - 500000
        S.append(sk)
    for k in range(56,4000000 + 1):
        sk = ( S[k-24] + S[k-55] + 1000000 ) % 1000000 - 500000
        S.append(sk)
    
    mat = np.zeros((2000,2000))
    for i in range(0,2000):
        for j in range(0,2000):
            mat[i,j] = S[i*2000+j]

    print 'solving'

    print 'finding greatest horizontal sum'
    a = greatest_horizontal_sum(mat)

    print 'finding greatest vertical sum'
    b = greatest_vertical_sum(mat)
   
    print 'finding greatest diagonal sum'
    c = greatest_diagonal_sum(mat)

    print 'finding greatest anti-diagonal sum'
    d = greatest_anti_diagonal_sum(mat)
    print (a,b,c,d)
    return max([a,b,c,d])    
        



if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans














