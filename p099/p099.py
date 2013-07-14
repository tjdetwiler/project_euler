
import numpy as np
import copy

def read_file(file_path):
    data = []
    with open(file_path) as fp:
      line = fp.readline()
      while line:
          line = line.split(',')
          data.append([int(line[0]),int(line[1])]) 
          line = fp.readline()
    return data


def main():
    data = read_file('base_exp.txt')
    pairs = []
    for pair in data:
        pairs.append(pair[1]*np.log10(pair[0]))
   
    sorted_pairs = copy.deepcopy(pairs)
    sorted_pairs.sort(reverse=True)
    max_val = sorted_pairs[0]
    max_index = pairs.index(max_val)    
    print '"""""""""""""""'
    print max_index +1

if __name__== "__main__":
  main()

