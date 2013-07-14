import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# http://en.wikipedia.org/wiki/Minimum_spanning_tree
# http://en.wikipedia.org/wiki/Kruskal%27s_algorithm

def read_file(file_path):
    with open(file_path) as fp:
      line = fp.readline() 

      xmat = []
      while line:
          line = line.strip('\n') 
          line = line.split(',')
          m = []
          for l in line:
              if l == '-':
                  m.append(0)
              else:
                  m.append(int(l))
          xmat.append(m)
          line = fp.readline()
    return np.array(xmat)


def DFS(G,a,c,b):
    #G is nx.Graph()
    # a is current vertex
    # c is vertex you came from
    # b is vertex in search for
    if a == b:
        return 1
    neighbors = G.neighbors(a)
    # print str(a) + ' neighbors: ' + str(neighbors)
    for x in neighbors:
        if x == c:
            continue
        result = DFS(G,x,a,b)
        if result:
            # print ' DFS = 1 for ' + str((x,b))
            return 1
    return 0
    


def is_cyclic(G,u,v):
    # u,v is the newly added edge 
    return DFS(G,v,u,u)

    

def solve():
    test = 0
    plot = 0
    if test:  
        mat = read_file('simple_network.txt')
    else:
        mat = read_file('network.txt')

    G = nx.from_numpy_matrix(mat)
    if plot:
        plt.figure(1)
        nx.draw(G)
    MST = nx.Graph()
    X = {}
    for edge in G.edges_iter():
        x = G[edge[0]][edge[1]]['weight']
        if x in X:
            X[x].append(edge)
        else:
            X[x] = [edge]

    original_weight = 0
    for e in G.edges_iter():
        original_weight += G[e[0]][e[1]]['weight']
    print 'original weight = ' + str(original_weight)

    for edge_weight in X:
        for edge in X[edge_weight]:
            MST.add_edge(edge[0],edge[1],weight=edge_weight)
            if is_cyclic(MST,edge[0],edge[1]):
                MST.remove_edge(edge[0],edge[1])
            if MST.number_of_edges() == G.number_of_nodes() - 1:
                minimized_weight = 0
                for e in MST.edges_iter():
                    minimized_weight += MST[e[0]][e[1]]['weight']
                print 'minimized weight = ' + str(minimized_weight)               
                if plot:
                    plt.figure(2)
                    nx.draw(MST)
                    plt.show()
                return original_weight - minimized_weight
            

 
    return -1


if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans





