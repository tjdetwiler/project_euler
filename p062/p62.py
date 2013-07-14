
def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def digits_to_num(digits):
    val = 0 
    j = 0
    for i in range(len(digits)-1,-1,-1):
        val += (10**i)*digits[j]
        j += 1
    return val

def get_digits(num):
    digit_count = 0;
    if num < 10:
        digit_count = 1
    elif num < 100:
        digit_count = 2
    elif num < 1000:
        digit_count = 3
    elif num < 10000:
        digit_count = 4
    elif num < 100000:
        digit_count = 5
    elif num < 1000000:
        digit_count = 6
    elif num < 10000000:
        digit_count = 7
    elif num < 100000000:
        digit_count = 8
    elif num < 1000000000:
        digit_count = 9
    elif num < 10000000000:
        digit_count = 10
    elif num < 100000000000:
        digit_count = 11
    elif num < 1000000000000:
        digit_count = 12
    elif num < 10000000000000:
        digit_count = 13
    elif num < 100000000000000:
        digit_count = 14
    else:
        print 'exceeded limit of get digits with ' + str(num)
        return []

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(r)
        t = t - r*p
    return digits

def greater_than(A,B):
    # return 1 if A > B
    l = len(A)
    for i in range(0,l):
        if A[i] > B[i]:
            return 1
        elif A[i] < B[i]:
            return 0
    return 0
            

def main():
    max_root = 10000
    cubes = []
    cubes_digits = []
    for i in range(0,max_root):
        v = i**3
        cubes.append(v)
        digits = get_digits(v)
        digits.sort()
        cubes_digits.append(digits)


    for i in range(0,len(cubes)):
        count = 0
        cube = cubes[i]

        digits = cubes_digits[i]
        X = []
        X.append(cube)
         
        for j in range(i+1,len(cubes_digits)):
            perm = cubes_digits[j]
            if digits == perm:
                val = cubes[j]
                count += 1
                X.append(val)
                if count == 4:
                    return cube
                   

if __name__== "__main__":
  result = main()
  print "***************"
  print result 
