import sys

def read_file(file_path):
    with open(file_path) as fp:
      data = fp.read()
    return data

if __name__== "__main__":

  ascii_offset = 64

  file_path = "names.txt"
  names = read_file(file_path)
  names = names.replace('\"','').split(",")
  names.sort()
  cum_sum = 0

  for i in range(0,len(names)):
     name = names[i]
     sum = 0
     for c in name:
         sum += ord(c)-ascii_offset
     cum_sum += sum*(i+1)
  print cum_sum
