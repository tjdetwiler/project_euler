import numpy as np
from collections import deque

# http://en.wikipedia.org/wiki/Dijkstra's_algorithm


INF = float('inf')

M =[[   7,  53, 183, 439, 863],
    [ 497, 383, 563,  79, 973],
    [ 287,  63, 343, 169, 583],
    [ 627, 343, 773, 959, 943],
    [ 767, 473, 103, 699, 303]]


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




def get_neighbors(mat,point):
    (m,n) = mat.shape
    (x,y) = point

    #top row
    if x == 0:
        # not first or last column
        if y != n-1 and y != 0:
            return [(x,y-1),(x,y+1),(x+1,y)]
        # last column
        elif y == n-1:
            return [(x,y-1),(x+1,y)]
        # first column
        else:
            return [(x,y+1),(x+1,y)]

    # bottom row
    elif x == m-1:
        # not first or last column
        if y != n-1 and y != 0: 
            return [(x,y-1),(x,y+1),(x-1,y)]
        # last column
        elif y == n-1:
            return [(x,y-1),(x-1,y)]
        # first column
        else:
            return [(x,y+1),(x-1,y)]

    # neither top or bottom row
    else:
        # not first or last column
        if y != n-1 and y != 0: 
            return [(x,y-1),(x+1,y),(x,y+1),(x-1,y)]
        # last column
        elif y == n-1:
            return [(x,y-1),(x+1,y),(x-1,y)]
        # first column
        else:
            return [(x,y+1),(x+1,y),(x-1,y)]


def Dijkstra(mat,source,target):
    (m,n) = mat.shape
    dist = np.zeros((m,n))
    previous = np.zeros((m,n,2))
    for i in range(0,m):
        for j in range(0,n):
            dist[i,j] = float('inf')
            previous[i,j] = None
    dist[source] = mat[source]

    Q = deque([source])
    while Q:
        u = Q.popleft()
        
        if u == target:
            break
        neighbors = get_neighbors(mat, u)
        for v in neighbors:
            alt = dist[u] + mat[v]
            if alt < dist[v]:
                dist[v] = alt
                previous[v] = u
                Q.append(v)


    path = []
    prev_pt = (target)

    while prev_pt[0] >=0 and prev_pt[1]>=0:
        (i,j) = prev_pt
        path.insert(0,mat[i,j])
        prev_pt = previous[i,j]

    # print (sum(path),path)
    return sum(path)

if __name__ == "__main__":
    min_val = float('inf')

    # mat = np.array([[131,673,234,103,18 ],
    #                 [201,96 ,342,965,150],
    #                 [630,803,746,422,111],
    #                 [537,699,497,121,956],
    #                 [805,732,524, 37,331]])

    mat = read_matrix()



    (m,n) = mat.shape
    source = (0,0)
    target = (m-1,n-1)
    val = Dijkstra(mat,source,target)
    print "********************"
    print val





