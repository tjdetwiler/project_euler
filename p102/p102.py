import sys

def read_file(file_path):
    triangles = []
    with open(file_path) as fp:
      line = fp.readline()
      while line:
          line = line.strip('\n')
          line = line.split(',')
          triangle = [(int(line[0]),int(line[1])),\
                      (int(line[2]),int(line[3])),\
                      (int(line[4]),int(line[5]))]
          triangles.append(triangle)
          line = fp.readline()
    return triangles


def in_bounding_rect(triange):
  x_vals = [triange[0][0],triangle[1][0],triangle[2][0]]
  y_vals = [triange[0][1],triangle[1][1],triangle[2][1]]
  if min(x_vals) > 0:
      return 0
  if max(x_vals) < 0:
      return 0
  if min(y_vals) > 0:
      return 0
  if max(y_vals) < 0:
      return 0
  return 1


def intersects(v1x1,v1y1,v1x2,v1y2,v2x1,v2y1,v2x2,v2y2):
    A1 = v1y1-v1y2
    B1 = v1x2-v1x1
    C1 = v1x1*v1y2 - v1x2*v1y1

    d1 = A1*v2x1 + B1*v2y1 + C1 
    d2 = A1*v2x2 + B1*v2y2 + C1 


    if d1 > 0 and d2 > 0:
        return 0
    if d1 < 0 and d2 < 0:
        return 0

    A2 = v2y1-v2y2
    B2 = v2x2-v2x1
    C2 = v2x1*v2y2 - v2x2*v2y1

    d1 = A2*v1x1 + B2*v1y1 + C2 
    d2 = A2*v1x2 + B2*v1y2 + C2 

    if d1 > 0 and d2 > 0:
        return 0
    if d1 < 0 and d2 < 0:
        return 0

    if A1*B2 - A2*B1 == 0:
        print "WARNING: COLLINEAR"
        return 0

    return 1


def contains_origin(triangle):
  (v1x1,v1y1) = (-10013,3)
  (v1x2,v1y2) = (0,0)  

  count = 0
  if in_bounding_rect(triangle):
      if intersects(v1x1,v1y1,v1x2,v1y2,triangle[0][0],triangle[0][1],triangle[1][0],triangle[1][1]):
          count +=1 
      if intersects(v1x1,v1y1,v1x2,v1y2,triangle[1][0],triangle[1][1],triangle[2][0],triangle[2][1]):
          count +=1 
      if intersects(v1x1,v1y1,v1x2,v1y2,triangle[2][0],triangle[2][1],triangle[0][0],triangle[0][1]):
          count +=1 
  if count == 1:
      return 1
  return 0


if __name__== "__main__":

  count = 0
  triangles = read_file("triangles.txt")
  for triangle in triangles:
      if contains_origin(triangle):
          count +=1 
      
  print "**************"
  print count
  

  

