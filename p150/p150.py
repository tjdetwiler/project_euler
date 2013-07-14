import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def get_node_count(rows):
    count = 0
    while rows:
        count += rows
        rows -= 1
    return count

def get_test_matrix():
    mat = np.zeros((6,6))
    mat[0,0] = 15
    mat[1,:2] = [-14,-7]
    mat[2,:3] = [20,-13,-5]
    mat[3,:4] = [-3,8,23,-26]
    mat[4,:5] = [1,-4,-5,-18,5]
    mat[5,:6] = [-16,31,2,9,28,3] 
    return mat

# def get_test_matrix():
#     mat = np.zeros((4,4))
#     mat[0,0] = 1
#     mat[1,:2] = [2,2]
#     mat[2,:3] = [3,3,3,]
#     mat[3,:4] = [4,4,4,4]
#     return mat


def print_mat(mat,x,y,z):
    (m,n) = mat.shape
    s = y + z
    # print ''
    # for i in range(s,m):
    #     print mat[i,y:m-z]
    # print ''

def get_triangular_matrix():
    # rows = 5
    # max_val = get_node_count(rows)
    max_val = 500500
    m = 1000
    # max_val = 28
    # m = 6
    mat = np.zeros((m,m),dtype=np.int32)
    two_twenty = np.power(2,20)
    two_nineteen = np.power(2,19)
    t = 0
    print 'calculating triangular matrix'
    print ''
    for i in range(0,m):
        for j in range(0,i):
            t = ( 615949*t + 797807 ) % two_twenty
            sk = t - two_nineteen            
            mat[i,j] = sk
    return mat

def get_sum(mat,x,y,z):
    (m,n) = mat.shape
    s = 0
    for i in range(y+z,m-x):
        s += np.sum(mat[i,y:n-z])
    return s


def get_mats(mat):
   (m,n) = mat.shape
   x_mat = np.zeros((m,n))
   y_mat = np.zeros((m,n))
   z_mat = np.zeros((m,n))
   
   for r in range(0,m):
       for i in range(r,m):
           z_mat[r,i-r] = mat[i,i-r]



   for r in range(0,m):
       x_mat[r,:] = mat[m-r-1,:]

   c = 0
   for r in range(0,m):
       y_mat[:,r] = x_mat[r,:]

   # print mat
   # print ""
   # print x_mat
   # print ""
   # print y_mat
   # print ""
   # print z_mat

   return (x_mat,y_mat,z_mat)

def solve():

    min_val = float('inf')
    mat = get_triangular_matrix()
    # mat = get_test_matrix()
    (xm,ym,zm) = get_mats(mat)
   
    (m,n) = mat.shape
    total = np.sum(mat)
    # print 'total = ' + str(total)
    # print xm[:1,:]
    # print ym[:1,:]
    # print total - np.sum(xm[:1,:]) - np.sum(ym[:1,1:] )
    
    # for x in range(0,m):
    #    x_tot = total - np.sum(xm[:x,:])
    #    for y in range(0,m-1-x):
    #        y_tot = x_tot - np.sum(ym[:y,x:])

    #        for z in range(0,m-1-x-y):
    #           print (x,y,z)
    #           val = y_tot - np.sum(zm[:z,x:m-y])
    #           # print (x,y,z,val)
    #           if val < min_val:
    #               min_val = val
    #               mc = (x,y,z) 
    #               # print (x,y,z,val)


    for x in range(-1,m):
       print x
       if x == -1:
           x_tot = total 
       else:
           # print 'x_tot previous = ' + str(x_tot)
           x_tot -= np.sum(xm[x,:])
           # print "x = " + str((x,xm[x,:],sum(xm[x,:]),x_tot))
        
       for y in range(-1,m-1-max(0,x)):
           if y == -1:
               y_tot = x_tot
               # print "y = " + str((y,ym[0,x+1:m],y_tot))
           else:
               # print 'y_tot previous = ' + str(y_tot)
               y_tot -= np.sum(ym[y,x+1:m-y])
               # print "y = " + str((y,ym[y,x+1:m-y],y_tot))
           
           for z in range(-1,m-max(0,x)-max(0,y)):
              if z == -1:
                  z_tot = y_tot
              else:
                  # print 'z_tot previous = ' + str(z_tot)
                  z_tot -= np.sum(zm[z,y+1:m-(x+1)-z])
                  # print "z = " + str((z,zm[z,y+1:m-(x+1)-z],z_tot))
              val = z_tot

              # print (x,y,z,val)

              if val < min_val:
                  min_val = val
                  mc = (x,y,z) 
                  # print (x,y,z,val)
   
    
    return min_val
  


if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans




