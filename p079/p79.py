import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def read_file(file_path):
    with open(file_path) as fp:
      line = fp.readline() 
      X = []
      while line:
          line = line.strip('\n') 
          X.append(int(line))
          line = fp.readline() 
    return X


def get_digits(num):
    digit_count = 0;
    if num < 10:
        digit_count = 1
    elif num < 100:
        digit_count = 2
    elif num < 1000:
        digit_count = 3
    elif num < 10000:
        digit_count = 4
    elif num < 100000:
        digit_count = 5
    elif num < 1000000:
        digit_count = 6
    elif num < 10000000:
        digit_count = 7
    elif num < 100000000:
        digit_count = 8
    elif num < 1000000000:
        digit_count = 9
    else:
        rem = 1
        digit_count = 10
        val = (10**digit_count)
        rem = num/val
        while rem != 0:
            digit_count += 1
            val = (10**digit_count)
            rem = num/val
        

    digits = []
    t = num
    for i in range(digit_count-1,-1,-1):
        p = 10**i
        r = t/p
        digits.append(int(r))
        t = t - r*p
    return digits

def traverse(G,a,path):
    #a is current vertex
    depth = len(path)
    max_depth = G.number_of_nodes()
    if depth == max_depth:
        return 1

    neighbors = G.neighbors(a)
    for n in neighbors:
        if n not in path:
            path.append(n)
            result = traverse(G,n,path)
            if result:
                return 1
            else:
                path.pop()
    return 0
            

def find_min_path(G):
    for n in G.nodes():
        path = [n]
        result = traverse(G,n,path)
        if result:
            return path
    return []


def solve():
    codes = read_file('keylog.txt')
    G = nx.DiGraph()
    for code in codes:
        digits = get_digits(code)
        G.add_path(digits)
        
    # for x in G.nodes():
    #     print (x,G.neighbors(x))
    # plt.figure(1)
    # nx.draw(G)
    # plt.show() 
    path = find_min_path(G)
j    return path


if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans





