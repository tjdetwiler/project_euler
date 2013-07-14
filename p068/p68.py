import sys
import itertools

def get_total(x):
    return sum([x[0],x[5],x[6]])

def is_magic(x):
    a = [x[0],x[5],x[6]]
    b = [x[1],x[6],x[7]]
    c = [x[2],x[7],x[8]]
    d = [x[3],x[8],x[9]]
    e = [x[4],x[9],x[5]]

    if sum(a) != sum(b):
        return 0
    if sum(b) != sum(c):
        return 0
    if sum(c) != sum(d):
        return 0
    if sum(d) != sum(e):
        return 0

    return 1
        
def get_solution_set(x):
    a = [x[0],x[5],x[6]]
    b = [x[1],x[6],x[7]]
    c = [x[2],x[7],x[8]]
    d = [x[3],x[8],x[9]]
    e = [x[4],x[9],x[5]]

    mv = min(a,b,c,d,e) 
    if mv == a:
        X = a+b+c+d+e
    if mv == b:
        X = b+c+d+e+a
    if mv == c:
        X = c+d+e+a+b
    if mv == d:
        X = d+e+a+b+c
    if mv == e:
        X = e+a+b+c+d

    Y = []
    for x in X:
        if x == 10:
            Y.append(1)
            Y.append(0)
        else:
            Y.append(x)   
    return Y

def greater_than(a,b):
    for i in range(0,len(a)):
        if a[i] > b[i]:
            return 1
        if a[i] < b[i]:
            return 0
    return 0 

def is_len_16(x):
    for v in x[:5]:
        if v == 10:
            return 1
    return 0


def solve():
    c = 0
    max_val = [0]*16
    for x in itertools.permutations(range(1,10+1)):
        if is_len_16(x):
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
  

  

