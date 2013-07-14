

def power_list(num,max_val):
    i = 1;
    x = i**num
    Y = []
    while x <= max_val:
        if x >= 10**(num-1) and x < 10**num:
            Y.append(x)
        i += 1
        x = i**num

    return Y

def main():
    
    #choose something large here...should exit when nothing is found 
    max_num_digits = 30
    X = []
    for i in range(1,max_num_digits+1):
        print 'checking ' + str(i) + ' digits'
        pl = power_list(i,10**i)

        if pl == []:
            print "empty list for num = " + str(i)
            return X
        else:
            for c in pl:
                X.append(c)
    return X






if __name__ == "__main__":
    X = main()
    print "************************"
    print len(X)
