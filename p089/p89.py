
def read_file(file_path):
    numerals = []
    with open(file_path) as fp:
      line = fp.readline()
      while line:
          line = line.strip('\n')
          numerals.append(line)
          line = fp.readline()
    return numerals


def decimal_val(char,prev_char):
    if char == 'I':
        if prev_char == 'V' or prev_char == 'X':
            return -1
        else:
            return 1
    elif char == 'V':
            return 5
    elif char == 'X':
        if prev_char == 'L' or prev_char == 'C':
            return -10
        else:
            return 10
    elif char == 'L':
            return 50
    elif char == 'C':
        if prev_char == 'D' or prev_char == 'M':
            return -100
        else:
            return 100
    elif char == 'D':
        return 500
    elif char == 'M':
        return 1000
    else:
        print "unknown char: " + str(char)
        exit(0)


def decimal_to_numeral(val):

    if val/1000 > 0:
        return "M" + decimal_to_numeral(val - 1000)
    elif val/900 > 0:
        return "CM" + decimal_to_numeral(val - 900)
    elif val/500 > 0:
        return "D" + decimal_to_numeral(val - 500)
    elif val/400 > 0:
        return "CD" + decimal_to_numeral(val - 400)
    elif val/100 > 0:
        return "C" + decimal_to_numeral(val - 100)
    elif val/90 > 0:
        return "XC" + decimal_to_numeral(val - 90)
    elif val/50 > 0:
        return "L" + decimal_to_numeral(val - 50)
    elif val/40 > 0:
        return "XL" + decimal_to_numeral(val - 40)
    elif val/10 > 0:
        return "X" + decimal_to_numeral(val - 10)
    elif val/9 > 0:
        return "IX" + decimal_to_numeral(val - 9)
    elif val/5 > 0:
        return "V" + decimal_to_numeral(val - 5)
    elif val/4 > 0:
        return "IV" + decimal_to_numeral(val - 4)
    elif val/1 > 0:
        return "I" + decimal_to_numeral(val - 1)
    else:
        return ""

        


def decode_roman_numeral(numeral):
    l = len(numeral)
    S = 0
    prev_char = None
    for i in range(l-1,-1,-1): 
        char = numeral[i]
        S += decimal_val(char,prev_char)
        prev_char = char
    return S
        


def main():
    S = 0
    numerals = read_file('roman.txt')
    for numeral in numerals:
        prev_char_count = len(numeral)
        val = decode_roman_numeral(numeral)
        minimized_numeral = decimal_to_numeral(val)
        minimized_char_count = len(minimized_numeral)
        diff = prev_char_count - minimized_char_count
        S += diff
    return S


if __name__== "__main__":
    val = main()
    print "**************"
    print val
