

import numpy as np

INF = float('inf')

def get_left_and_up(mat,point):
    # print point
    i = point[0]
    j = point[1]
    (m,n) = mat.shape                
    if i == 0 and j == 0:
        return(0,0)
    if i == 0:
        return (mat[i,j-1],INF)
    if j == 0:
        return (INF,mat[i-1,j])
    return (mat[i,j-1],mat[i-1,j])

def get_right_and_up(mat,point):
    # print point
    i = point[0]
    j = point[1]
    (m,n) = mat.shape
    if i == 0 or j == n-1:
        return None
    return (i-1,j+1)
                   

def get_next_starting_pt(mat,point):
    # print point
    i = point[0]
    j = point[1]
    (m,n) = mat.shape
    if i == m-1:
        if j == n-1:
            return None
        return (i,j+1)
                   
    else:
        return (i+1,j)                  

def get_min_path_sum(mat):
    (m,n) = mat.shape
    starting_point = (0,0)
    while starting_point:
        # print 'starting point ' + str(starting_point)       
        point = starting_point
        while point:
            previous = get_left_and_up(mat,point)
            # print 'previous points of  ' + str(point) + ' = ' + str(previous)
            val = mat[point]
            new_val = min(previous[0],previous[1]) + val
            mat[point] = new_val
            point = get_right_and_up(mat,point)
        # print mat
        starting_point = get_next_starting_pt(mat,starting_point)
    return mat[m-1,n-1]
    


def test():
    mat = np.array([ [131,673,234,103,18 ],
                   [201,96 ,342,965,150],
                   [630,803,746,422,111],
                   [537,699,497,121,956],
                   [805,732,524, 37,331]],
                   dtype=np.int16 )
    (m,n) = mat.shape
    path_sum = get_min_path_sum(mat)
    print "********************"
    print path_sum
    


def read_matrix():
    file = "matrix.txt"
    f = open(file,'r')
    line = f.readline()
    mat = np.zeros((80,80),dtype=np.int32)
    row = 0
    while line:
        nums = line.split(',')
        col = 0
        for val in nums:
            mat[row,col] = int(val)
            col += 1
        row += 1
        line = f.readline()

    f.close()
    return mat

if __name__ == "__main__":

    mat = read_matrix()
    path_sum = get_min_path_sum(mat)
    print "********************"
    print path_sum





