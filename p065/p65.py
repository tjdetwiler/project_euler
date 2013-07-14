
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
        rem = float(num)/val
        while rem >= 1:
            digit_count += 1
            val = (10**digit_count)
            rem = float(num)/val
        

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(int(r))
        t = t - r*p
    return digits

def main():
   A = [2,1,2,1,1,4,1,1,6,1,1,8]
   A = [2]
   for i in range(2,100,2):
       A.append(1)
       A.append(i)
       A.append(1)
   A = A[0:101]
   
   c = 1
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
           # print(x,y,z)
       num = z*x+y
       den = z
       # print(c,num,den)
       c += 1 
   return num

if __name__== "__main__":
    num = main()
    digits = get_digits(num)
    print num
    print ""
    print digits
    print "*****************"
    print sum(digits)

