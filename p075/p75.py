import numpy as np

# http://en.wikipedia.org/wiki/Tree_of_Pythagorean_triples

A = np.array([[1,-2,2],
              [2,-1,2],
              [2,-2,3]])            
B = np.array([[1,2,2],
              [2,1,2],
              [2,2,3]])            
C = np.array([[-1,2,2],
              [-2,1,2],
              [-2,2,3]])            

def get_children(x):
    return(np.dot(A,x),np.dot(B,x),np.dot(C,x))
    
    
def get_non_primitives(tri,Ps,thresh):
    i = 1
    P = sum(tri) 
    if P <= thresh:
        while P <= thresh:
            if P in Ps:
                Ps[P] += 1
            else:
                Ps[P] = 1             
            i += 1
            P += sum(tri)
    
     
        
    
def find_triangles():
    thresh = 1500000
    Ps = {}
    x = None
    leaves = [np.array([3,4,5])]
    
    get_non_primitives(leaves[0],Ps,thresh)
    
    while leaves:
        next_leaves = []
    
        for leaf in leaves:
            children = get_children(leaf)
            for child in children:
                get_non_primitives(child,Ps,thresh)
                P = sum(child) 
                if P <= thresh:
                    next_leaves.append(child) 
        leaves = next_leaves
    
    return Ps
       
def solve():
    print "will take ~2-4 minutes runtime"
    tris = find_triangles()
    cnt = 0
    for t in tris:
        if tris[t] == 1:
            cnt += 1
    return cnt
    
if __name__ == "__main__":
    ans = solve()
    print "**************"
    print ans
