
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
    else:
        rem = 1
        digit_count = 10
        val = (10**digit_count)
        rem = num/val
        while rem != 0:
            digit_count += 1
            val = (10**digit_count)
            rem = num/val
        

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(int(r))
        t = t - r*p
    return digits

def main():
   expansions = 1000
   A = [1] + [2]*(expansions+1)
   # A = [1,2,2,2,2,2,2,2]
   num_exceed_count = 0
   c = 2
   while c < len(A):
       a = A[:c]
       l = len(a);
       index = l-2
       x = a[index]
       y = 1
       z = a[index+1]
       while index > 0:
           index -= 1
           zp = z
           z = z*x+y
           y = zp
           x = a[index]
       num = z*x+y
       den = z
       # print(c-1,num,den)
       num_digits = get_digits(num)
       den_digits = get_digits(den)
       if len(num_digits) > len(den_digits):
           num_exceed_count += 1
       c += 1 
   return num_exceed_count

if __name__== "__main__":
    num = main()
    print "*****************"
    print num

