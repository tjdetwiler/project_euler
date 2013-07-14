import numpy as np
import os

# http://www.youtube.com/watch?v=p-gpaIGRCQI




S = [[0,0,3,0,2,0,6,0,0],
     [9,0,0,3,0,5,0,0,1],
     [0,0,1,8,0,6,4,0,0],
     [0,0,8,1,0,2,9,0,0],
     [7,0,0,0,0,0,0,0,8],
     [0,0,6,7,0,8,2,0,0],
     [0,0,2,6,0,9,5,0,0],
     [8,0,0,2,0,3,0,0,9],
     [0,0,5,0,1,0,3,0,0]]

# --------------------------------------------#

def digits_to_num(digits):
    val = 0 
    j = 0
    for i in range(len(digits)-1,-1,-1):
        val += (10**i)*digits[j]
        j += 1
    return val

# --------------------------------------------#


class MatrixGen(object):
    
    def __init__(self):
        self.fp = open("sudoku.txt")

    def next_matrix(self):  
        line = self.fp.readline()
        if not line:
            self.fp.close()
            return None
        mat = np.zeros((9,9),dtype=np.int16)
        for i in range(0,9):
            line = self.fp.readline()
            for j in range(0,9):
                mat[i,j] = int(line[j])
        
        return mat

# --------------------------------------------#

def no_conflicts(mat,point,val):
    (x,y) = point
    row_vals = mat[x,:]
    if val in row_vals:
        return 0
    col_vals = mat[:,y]
    if val in col_vals:
        return 0
    xx = (x/3)*3
    yy = (y/3)*3
    submat = mat[xx:xx+3,yy:yy+3]
    submat = submat.ravel()
    if val in submat:
        return 0
    return 1

# --------------------------------------------#
        
def check_puzzle(mat):
    (m,n) = mat.shape
    for x in range(0,m):
        if len(set(mat[x,:])) != 9:
            return 0
    for y in range(0,n):
        if len(set(mat[:,y])) != 9:
            return 0
    for x in range(0,9,3):
        for y in range(0,9,3):
            z = mat[x:x+3,y:y+3].ravel()
            if len(set(z)) != 9:
                return 0
    return 1

# --------------------------------------------#

def solve_sudoku(mat,point,c):
    (m,n) = mat.shape
    def get_next_point():
        (x,y) = point
        while True:  
            if y<n-1:
                y += 1
                if mat[x,y] != 0:
                    continue
                return (x,y)
            else:
                if x<m-1:
                    x += 1
                    y = 0
                    if mat[x,y] != 0:
                        continue
                    return (x,y)
                else:
                    return None 
    if mat[point] != 0:
        point = get_next_point()
    for val in range(1,10):
        if no_conflicts(mat,point,val):
            mat[point] = val 
            next_point = get_next_point()

            if c == 16:
                os.system('clear') 
                print c
                print mat

            if next_point:
                result = solve_sudoku(mat,next_point,c)
                if result:
                    return 1
                else:
                    mat[point] = 0
            else:
                return 1
    return 0        
            
        
# --------------------------------------------#

if __name__ == "__main__":
     M = MatrixGen()
     mat = M.next_matrix()
     c = 0
     S = 0
     while mat is not None:
         if c == 15:
            print mat 
         result = solve_sudoku(mat,(0,0),c+1)
         if result == 0:
             print "puzzle not solved: number " + str(c+1)
             exit(0)
         result = check_puzzle(mat)
         if result == 0:
             print "puzzle check failed: number " + str(c+1)
             exit(0)
         digits = mat[0,0:3]
         val = digits_to_num(digits)
         S += val
         c +=1   
         print (c,val)
         mat = M.next_matrix()

     print "**********"
     print S
