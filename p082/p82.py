import numpy as np
from collections import deque


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
    if x == 0:
        if y != n-1:
            return [(x,y+1),(x+1,y)]
        else:
            return [(x+1,y)]
    elif x == m-1:
        if y != n-1:
            return [(x-1,y),(x,y+1)]
        else:
            return [(x-1,y)]
    else:
        if y != n-1:
            return [(x-1,y),(x,y+1),(x+1,y)]
        else:
            return [(x-1,y),(x+1,y)]


def Dijkstra(mat,source):
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
        neighbors = get_neighbors(mat, u)
        # print "neighbors of " + str(u) + " = " + str(neighbors)
        for v in neighbors:
            alt = dist[u] + mat[v]
            # print 'alt to ' + str(v) + ' -- (' + str(mat[v]) +\
            #       ') from ' + str(u) + ' -- (' + str(mat[u]) + ') is ' + str(alt)
            # print ' ...currently ' + str(dist[v]) 
            if alt < dist[v]:
                # print 'dist to ' + str(v) + ' is ' + str(alt)
                dist[v] = alt
                # print 'prev to ' + str(v) + ' is ' + str(u)
                # print previous[:,0]
                previous[v] = u
                Q.append(v)

    mn = min(dist[:,n-1])
    i = np.where(dist == mn)

    # if len(i[0]) > 1:
    #     print "more than one min"

    path = []
    prev_pt = (i[0][0],i[1][0])

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
    for i in range(0,m):
        print i
        source = (i,0)
        val = Dijkstra(mat,source)
        if val < min_val:
            min_val = val
    print "********************"
    print min_val





