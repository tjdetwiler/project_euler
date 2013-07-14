

def main():
    
    max_n = 1000000

    print "computing triangles..."
    tri = []
    for i in range(140, max_n+1):
        y = i*(i+1)/2
        tri.append(y)
    
    print "computing pentagonals..."
    pent = []
    for i in range(140, max_n+1):
        y = i*(3*i-1)/2
        pent.append(y)
    
    print "computing hexagonals..."
    hexag = []
    for i in range(140, max_n+1):
        y = i*(2*i-1)
        hexag.append(y)
    
    tri = set(tri)
    pent = set(pent)
    hexag = set(hexag)

    x1 = tri.intersection(pent)
    x2 = x1.intersection(hexag)
    
    x2 = list(x2)
    print x2
    



if __name__ == "__main__":
    main()
