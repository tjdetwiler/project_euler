



def get_rectangle_count(m,n):
    return .25*(m*n*(m+1)*(n+1))



def main():
    m = 1
    n = 1
    min_diff = float("inf")
    target = 4000000
    mm = 0
    nn = 0
    while True:
        n = 1
        c = get_rectangle_count(m,n)
        while c < target:
            c = get_rectangle_count(m,n)
            diff = abs(2000000-c)
            if diff < min_diff:
                min_diff = diff
                mm = m
                nn = n
            n+=1
        if n==1:
            break    
        m += 1
    return (mm,nn)
    



if __name__ == "__main__":
    (mm,nn) = main()
    c = get_rectangle_count(mm,nn)
    diff = abs(2000000-c)
    print "*****************"
    print mm*nn
