
def read_file(file_path):
    with open(file_path) as fp:
      data = fp.read()
    return data


if __name__== "__main__":

  max_word_val = 30
  print "making triangle numbers..."
  triangle_numbers = [x*(x+1)/2 for x in range(1,max_word_val+1)]
  ascii_offset = 64
  file_path = "words.txt"
  print "reading words..."
  words = read_file(file_path)
  words = words.replace('\"','').split(",")


  X = []
  max_val = 0
  print "finding triangle words..."
  for word in words:
     word_value = 0
     for c in word:
         word_value += ord(c)-ascii_offset
     if word_value > max_val:
         max_val = word_value
     if word_value in triangle_numbers:
         X.append(word_value)

  print "*******************"
  print len(X)
