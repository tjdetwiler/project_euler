

def is_concealed_square(s):
    l = 19
    if len(s) == l:
        # print 'is long enough'
        r = ['1','2','3','4','5','6','7','8','9','0']
        c = 0
        for i in range(0,l,2):
            # print str(s[i]) +' v ' + str(r[c])
            if s[i] != r[c]:
                return 0
            c += 1
        return 1
    elif len(s) > l:
            print "over length 19"
            exit(1)
    return 0    


def main():
    i = int(1e9)
    while True:
        if i % 1000000 == 0:
            print i
        val = i**2
        str_val = str(val)
        if is_concealed_square(str_val):
            
            return (i,str_val)
        i += 10


if __name__ == "__main__":
    (val,sq) = main()
    print "************************"
    print (val,sq)
    # v = '1828384858687882923'
    # print is_concealed_square(v)
