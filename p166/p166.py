import numpy as np
import time

def get_subset(entire_set,position_vals_array):
  subset = []
  for x in entire_set:
    match = 1
    for (p,v) in position_vals_array:
      if x[p] != v:
        match = 0
        break
    if match:
      subset.append(x)
  return subset

def get_set(S):
  X = []
  D = range(0,10)
  for a in D:
    for b in D:
      for c in D:
        for d in D:
            if a+b+c+d == S:
                X.append((a,b,c,d))
  return X
   
def check_column_sums(M,S):
  for col in range(0,4):
    if sum(M[:,col]) > S:
      return 0
  return 1

def has_criss_cross(M,S):
  for col in range(0,4):
    if sum(M[:,col]) != S:
      return 0
  return 1

def count_mixtures(S):
  count = 0
  M = np.zeros((4,4))
  X = get_set(S)
  for a in X:
    M[0,:] = a
    for b in get_subset(X,[ (0,a[0]) ]):
      M[1,1] = b[1]; M[2,2] = b[2]; M[3,3] = b[3]
      if not check_column_sums(M,S):
        M[1,1] = 0; M[2,2] = 0; M[3,3] = 0;
        continue
      for c in get_subset(X,[ (0,a[3]) ]):
        M[1,2] = c[1]; M[2,1] = c[2]; M[3,0] = c[3]
        if not check_column_sums(M,S):
          M[1,2] = 0; M[2,1] = 0; M[3,0] = 0;
          continue
        for d in get_subset(X,[ (1,b[1]), (2,c[1]) ]):
          M[1,0] = d[0]; M[1,3] = d[3]; 
          if not check_column_sums(M,S):
            M[1,0] = 0; M[1,3] = 0; 
            continue
          for e in get_subset(X,[ (1,c[2]), (2,b[2]) ]):
            M[2,0] = e[0]; M[2,3] = e[3]; 
            if not check_column_sums(M,S):
              M[2,0] = 0; M[2,3] = 0;
              continue
            for f in get_subset(X,[ (0,c[3]), (3,b[3]) ]):
              M[3,1] = f[1]; M[3,2] = f[2]; 
              if has_criss_cross(M,S):
                count += 1
            M[3,1] = 0; M[3,2] = 0; 
          M[2,0] = 0; M[2,3] = 0;
        M[1,0] = 0; M[1,3] = 0; 
      M[1,2] = 0; M[2,1] = 0; M[3,0] = 0;
    M[1,1] = 0; M[2,2] = 0; M[3,3] = 0;
  M[0,:] = [0,0,0,0];
  return count

def solve():
  total_count = 0
  for S in range(0,4*9 + 1):
    c = count_mixtures(S)
    total_count += c
    print (S,c,total_count)

  return total_count

if __name__ == "__main__":
  start = time.time()
  result = solve()
  stop = time.time()
  print "**********"
  print result
  print "runtime: " + str(stop-start) + " sec."



# (0, 1, 1)                                     │
# (1, 8, 9)                                     │
# (2, 48, 57)                                   │
# (3, 200, 257)                                 │
# (4, 675, 932)                                 │
# (5, 1904, 2836)                               │
# (6, 4736, 7572)                               │
# (7, 10608, 18180)                             │
# (8, 21925, 40105)                             │
# (9, 42328, 82433)                             │
# (10, 76976, 159409)                           │
# (11, 131320, 290729)                          │
# (12, 209127, 499856)                          │
# (13, 309968, 809824)                          │
# (14, 427440, 1237264)                         │
# (15, 549184, 1786448)                         │
# (16, 658457, 2444905)                         │
# (17, 736744, 3181649)
# (18, 766736, 3948385)

# ans = 3948385 + 3181649
