def gcd(a, b):
    while b != 0:
       t = b
       b = a % t
       a = t
    return a


def solve():
    maxd = 12000
    count = 0
    for d in range (3,maxd +1):
        if d % 1000 == 0:
            print d
        for n in  range(d/3+1,d/2+1):
            if gcd(d,n) == 1:
                count +=1 
                # print (n,d)
    return count
           
                        
                    
    



if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans
