#
# Project Euler
# Problem 15

# Start at the top left corner of the matrix
# in each node, sum the number of paths that reach
# the nodes to the left and above a given node
#

import sys
import copy
import numpy as np

def main(dim):
  dim = dim +1
  X = np.ones((dim,dim));
  X[0,0] = 2;

  for k in range(1,dim):
      for j in range(k,dim):
          X[k,j] = X[k-1,j] + X[k,j-1]
      for j in range(k,dim):
          X[j,k] = X[k-1,j] + X[k,j-1]


  return X[dim-1,dim-1ls]

if __name__  == "__main__":
    dim = int(sys.argv[1]);
    count = main(dim)
    print "count = " + str(count)
