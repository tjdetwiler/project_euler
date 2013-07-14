
odds = ['1','3','5','7','9']
evens = ['0','2','4','6','8']

def check_ends(x):
    l = len(x)
    a = x[0]
    b = x[l-1]
    if a in odds and b in evens:
        return 1
    if b in odds and a in evens:
        return 1
    return 0


def main():
    print "NOTE: runtime ~40min"
    print "....very poor algorithm in terms of complexity"
    X = []
    count  = 0
    max_val = int(1e9)
    print 'beginning search..'
    for i in xrange(0,max_val):
        if i % 1000000 == 0:
            print i

        if i % 10 == 0:
            continue

        v = i
        strv = str(v)


        rev_strv = strv[::-1]
        rev_v = int(rev_strv)
        if rev_v < v:
            continue

        if not check_ends(strv):
            continue

        y = v + rev_v
        x = str(y)
        is_rev = 1
        for t in x:
            if t not in odds:
                is_rev = 0
                break
        if is_rev:
            if v == rev_v:  
                count += 1
            else:
                count += 2
        # if is_rev:
        #     if v == rev_v:  
        #         X.append(v)
        #     else:
        #         X.append(v)
        #         X.append(rev_v)
            

    return count

if __name__  == "__main__":
    X = main()
    print "*********************"
    print X


