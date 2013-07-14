def digits_to_num(digits):

    val = 0 
    j = 0
    for i in range(len(digits)-1,-1,-1):
        val += (10**i)*digits[j]
        j += 1
    return val

def is_increasing(digits):
    for i in range(1,len(digits)):
        if digits[i] > digits[i-1]:
            return 0
    return 1

def is_decreasing(digits):
    for i in range(1,len(digits)):
        if digits[i] < digits[i-1]:
            return 0
    return 1
        

def is_bouncy(digits):
    if len(digits) < 3:
        return 0
    if is_increasing(digits):
        return 0
    if is_decreasing(digits):
        return 0
    return 1

def increment(digits,index):
    l = len(digits)
    if l == index:
        digits.insert(index,1)
        return
    v = digits[index]
    if v < 9:
       digits[index] += 1
    else:
       digits[index] = 0
       increment(digits,index+1)
    

def calculate():
    digits = [0]
    l = len(digits)
    frac = 0.0    
    num = 0.0
    den = 0.0
    while frac != .99:
        increment(digits,0)
        r = is_bouncy(digits)
        den += 1.0
        if r:
            num += 1.0
        frac = num/den

    digits = digits[::-1]
    digits = [int(d) for d in digits]
    val = digits_to_num(digits)
    print "****************"
    print val    


           



if __name__== "__main__":
    calculate()
