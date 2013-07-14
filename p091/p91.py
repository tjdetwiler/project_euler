import time
import numpy as np

# runtime ~75 sec

DIM = 50

def is_right_triangle(A,B):
    a = np.sqrt( (A[0]**2)+(A[1]**2))
    b = np.sqrt( (B[0]**2)+(B[1]**2))
    c = np.sqrt( ((A[0]-B[0])**2)+((A[1]-B[1])**2) )
    side_lengths = [a,b,c]

    if c == 0.0:
        return 0

    side_lengths.sort()
    a =  side_lengths[0]
    b =  side_lengths[1]
    c =  side_lengths[2]

    d = a**2 + b**2
    if np.abs(d-c**2)< 1e-5:
        return 1
    return 0

def get_next_points(A,B):
    global DIM 

    (x0,y0) = A
    (x1,y1) = B
    
    if y1 < DIM:
        return (A,(x1,y1+1))
    elif x1 < DIM:
        return (A,(x1+1,0))

    elif y0 < DIM:
        return ((x0,y0+1),(x0,y0+1))
    elif x0 < DIM:
        return ((x0+1,0),(x0+1,0))
    else:
        return None


def solve():
    global DIM 
    DIM = 50
    last_count = 0
    while DIM < 51:
        count = 0
        A = (0,1)
        B = (1,0)

        while True:
            if is_right_triangle(A,B):
                count += 1

            next_pts = get_next_points(A,B)
            if not next_pts:
                return count
            (A,B) = next_pts

        DIM += 1
         
      
        

if __name__== "__main__":
  start = time.time()
  ans = solve()
  print "**************"
  stop = time.time()
  print ans
  print 'runtime: ' + str(stop-start) + ' sec.'
  

  
