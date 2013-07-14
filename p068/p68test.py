import sys
import itertools

def get_total(x):
    return sum([x[0],x[5],x[6]])

def is_magic(x):
    a = [x[0],x[3],x[4]]
    b = [x[1],x[4],x[5]]
    c = [x[2],x[5],x[3]]

    if sum(a) != sum(b):
        return 0
    if sum(b) != sum(c):
        return 0

    return 1
        
def get_solution_set(x):
    a = [x[0],x[3],x[4]]
    b = [x[1],x[4],x[5]]
    c = [x[2],x[5],x[3]]
    if min(a,b,c) == a:
        return a+b+c
    if min(a,b,c) == b:
        return b+c+a
    if min(a,b,c) == c:
        return c+a+b

def greater_than(a,b):
    for i in range(0,len(a)):
        if a[i] > b[i]:
            return 1
        if a[i] < b[i]:
            return 0
    return 0 


def solve():
    c = 0
    max_val = [0]*9
    for x in itertools.permutations(range(1,6+1)):
        c += 1
        if is_magic(x):
            a = get_solution_set(x)
            if greater_than(a,max_val):
                print (c,a)
                max_val = a

    return max_val
    
    


if __name__== "__main__":

  ans = solve()
  print "**************"
  print ans
  

  

