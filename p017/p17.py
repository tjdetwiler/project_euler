import sys
from words import *




ONES_DIGITS = [ONE,TWO,THREE,FOUR,FIVE,SIX,SEVEN,EIGHT,NINE]
TEENS = [TEN,ELEVEN,TWELVE,THIRTEEN,FOURTEEN,FIFTEEN,SIXTEEN,SEVENTEEN,\
         EIGHTEEN,NINETEEN]
TENS_DIGITS = [TWENTY,THIRTY,FORTY,FIFTY,SIXTY,SEVENTY,EIGHTY,NINETY]



sum = 0;

# 0-9
for d in ONES_DIGITS:
  print d
  sum += len(d)

# 10-19
for d in TEENS:
  print d
  sum += len(d)

# 20-99
for d in TENS_DIGITS:
    print d
    sum += len(d)
    for t in ONES_DIGITS:
        print d + t
        sum += len(d+t)

# 100-999
for h in ONES_DIGITS:
    #100
    hh = h + HUNDRED
    print hh
    sum += len(hh)
    
    #101-109
    for t in ONES_DIGITS:
        y = hh+AND_WORD+t
        print y
        sum += len(y)

    # 110-119
    for d in TEENS:
      y = hh+AND_WORD+d
      print y
      print len(y)
      sum += len(y)

    # 120-999
    for d in TENS_DIGITS:
        y = hh+AND_WORD+d
        print y 
        sum += len(y)
        for t in ONES_DIGITS:
            z =  y + t
            print z
            print len(z)
            sum += len(z)
            print sum


print ONE+THOUSAND
sum += len(ONE+THOUSAND)
print sum
