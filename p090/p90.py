import scipy.misc as misc
import itertools

def can_make_value(setA,setB,value):
  a = value/10;
  b = value - 10*a
  
  if a == 6:
    a = 9

  if b == 6:
    b = 9

  if a in setA and b in setB:
    return True

  if b in setA and a in setB:
    return True

  return False

def can_make_all_squares(setA,setB):
  squares = [1,4,9,16,25,36,49,64,81]
  for square in squares:
    if not can_make_value(setA,setB,square):
      return False
  return True


def solve() :

  n = range(10)
  n = [0,1,2,3,4,5,9,7,8,9]
  X = list(itertools.combinations(n,6))
  
  count = 0
  for i in range(0, len(X)):
    for j in range(i+1,len(X)):
      setA = X[i]
      setB = X[j]
      if can_make_all_squares(setA,setB):
        count += 1

  return count


if __name__ == "__main__":
  ans = solve();
  print "***************"
  print ans

