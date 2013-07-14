import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def get_node_count(rows):
    count = 0
    while rows:
        count += rows
        rows -= 1
    return count

def get_main_graph():
    # rows = 5
    # max_val = get_node_count(rows)
    max_val = 500500
    
    S = []
    two_twenty = np.power(2,20)
    two_nineteen = np.power(2,19)
    t = 0
    print 'calculating pseudo random numbers'
    for k in range(0,max_val):
        t = ( 615949*t + 797807 ) % two_twenty
        sk = t - two_nineteen
        S.append(sk)

    R = {}
    index = 0
    G = nx.DiGraph()
    i = 0
    G.add_node(S[i])
    prev_row = [S[i]]
    R[1] = [S[i]]
    i += 1
    while i != len(S):
        row = []

        for node in prev_row:
            child = S[i]
            if child not in row:
                row.append(child)
            G.add_node(child)        
            G.add_edge(node,child)
            child = S[i+1]
            if child not in row:
                row.append(child)
            G.add_node(child)        
            G.add_edge(node,child)
            i += 1
        i += 1   
        R[len(row)] = row      
        prev_row = row



    return (G,R)


def get_min_subtriangle_value(G,top_node):
    min_sum = top_node
    neighbors = list(nx.neighbors(G,top_node))
    s = top_node
    row = 2
    while neighbors:

        # print row 
        # print neighbors
        # print ""

        next_neighbors = []
        row += 1
        s += sum(neighbors)
        if s < min_sum:
            min_sum = s
        for node in neighbors:
            next_neighbors += list(nx.neighbors(G,node))

        next_neighbors = list(set(next_neighbors))
        neighbors = next_neighbors


    return min_sum
        
                       



def solve():
    (G,R) = get_main_graph()
    print 'max = ' +  str(max([k for k in R]))
    min_val = float('inf')
    print 'fiding minimum sub triangle'
    for r in R:
        print r
        for node in R[r]:
            val = get_min_subtriangle_value(G,node)
    if val < min_val:
        min_val = val

    return min_val            


if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans




