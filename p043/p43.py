

def digits_to_num(digits):

    val = 0 
    j = 0
    for i in range(len(digits)-1,-1,-1):
        val += (10**i)*digits[j]
        j += 1
    return val
        

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]





def is_div_by_val(digits,val):
    if val == 2:
        if digits[2] % 2 == 0:
            return 1
        return 0
    elif val == 3:
        if sum(digits) % 3 == 0:
            return 1
        return 0
    elif val == 5:
         if digits[2] == 0 or digits[2] == 5:
             return 1
         return 0
    else:
        num = digits_to_num(digits)
        if num % val == 0:
            return 1
        return 0


def is_substring_divisible(digits):
    divs = [2,3,5,7,11,13,17]
    for i in range(0,len(divs)):
        if not is_div_by_val(digits[i+1:i+4],divs[i]):
            return 0
    return 1


if __name__ == "__main__":

    X = []
    digits = [0,1,2,3,4,5,6,7,8,9]
    perms = all_perms(digits)

    for perm in perms:
        if is_substring_divisible(perm):
            X.append(perm)
    YY = list(X)

    Z = []
    for y in YY:
        Z.append(digits_to_num(y))
    print "********************"
    print sum(Z)
