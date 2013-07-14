import numpy as np

def digits_to_num(digits):
    val = 0 
    j = 0
    for i in range(len(digits)-1,-1,-1):
        val += (10**i)*digits[j]
        j += 1
    return val


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


def read_file(file_path):
    with open(file_path) as fp:
      data = fp.read()
      data = data.split(',')
      words = []
      for x in data:
          xx = x.strip('"')
          # z = []
          # for y in xx:
          #     z.append(ord(y))
          # z.sort()
          # z = tuple(z)
          z = xx
          words.append(z)
    return words


def sort_words(words):
    sorted_words = {}
    for word in words:
        l = len(word)
        if l in sorted_words:
            sorted_words[l].append(word)
        else:
            sorted_words[l]= [word]
    return sorted_words

def get_squares_lists(longest):
    i = 1
    squares = {}
    while True:
        sq = np.power(i,2)
        digits = get_digits(sq)
        l = len(digits)
        if l > longest:
            return squares
        if l in squares:
            squares[l].append(digits)
        else: 
            print len(digits)
            squares[l] = [digits]
        i += 1

def get_word(ords):
    st = ""
    for o in ords:
        st += chr(o)
    return st


def find_anagram_squares(words,word_len):
    X = []
    for word in words:
        y = []
        for letter in word:
            y.append(ord(letter))
        y.sort()
        X.append(tuple(y))
    Y = []
    for i in range(0,len(words)):
        w1 = X[i]
        for j in range(i+1,len(words)):
            w2 = X[j]
            if w1 == w2:
                word1 = words[i]
                word2 = words[j]
                if word1 != word2:
                    Y.append((word1,word2))

    return Y

def square_is_candidate(word,num):
    digits = get_digits(num)
    if 0 in digits:
        return 0
    for i in range(0,len(word)):
        index = word.index(word[i])
        if digits.index(digits[i]) != index:
            return 0
    return 1


        

def is_square_anagram(pair,val):
    orig_val = val
    word1_sq_digits = get_digits(val)
    (word1,word2) = pair
    digits = []
    for letter in word2:
        index = word1.index(letter)
        val = word1_sq_digits[index]
        digits.append(val)
    val = digits_to_num(digits)
    if np.sqrt(val) % 1.0 < 1e-5:
        return val
    return 0 
         



def find_largest_pair_number(pair):
    max_val = 0
    (word1,word2) = pair
    l = len(word1)
    
    min_root = int(np.ceil(np.sqrt(np.power(10,l-1))))
    max_root = int(np.floor(np.sqrt(np.power(10,l))))
    for i in range(max_root,min_root -1, -1):
        val = int(np.power(i,2))
        if square_is_candidate(word1,val):
            word2_sq = is_square_anagram(pair,val)
            if word2_sq:
                m = max(val,word2_sq)
                if m > max_val:
                    max_val = m
                    a = val
                    b = word2_sq
    return max_val
        
        

if __name__== "__main__":
  ans = None
  word_len = 14
  words = read_file('words.txt')
  sorted_words = sort_words(words)
  for word_len in range(14,0,-1):
      pairs = find_anagram_squares(sorted_words[word_len],word_len)
      for pair in pairs:
          val = find_largest_pair_number(pair)
          if val:
              print "*********************"
              print val 
              exit(0)
  

