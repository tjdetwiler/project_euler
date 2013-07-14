import sys
import time


def print_sequence(L,P):
    return
    out = ['['] + [' ']*L + [']']
    for (next_tile_index,tile_length) in P:
        for i in range(0,tile_length):
            out[next_tile_index+i+1]=unichr(9724)
    print "".join(out)



def tile_count(L,index,P,m):
    if index >= L :
        return 0
    Porig = P
    count = 0
    while index <= L-3:
        max_tile_length = L-index

        for tile_length in range(m,max_tile_length+1):
            count +=1
            P = Porig + [(index,tile_length)]
            print_sequence(L,P)
            count += tile_count(L,index+tile_length+1,P,m)

        index += 1

    return count    

def solve(L):
    d2 = 17
    d1 = 28
    x = [0,-1,-1,0,1,1]
    i = 0
    l = 11
    val = 72
    while l <= L:
        d = d1+d2+x[i]
        val += d
        # print (l,val,d1,d2,d)
        i = (i+1)%len(x)
        l += 1
        d2 = d1
        d1 = d
    return val

# slow way
def solve2(L,m):
    count = 1
    print_sequence(L,[])
    count += tile_count(L,0,[],m)
    return count



if __name__== "__main__":
  L = 167
  ans = 0
  m = 50
  while ans < 1000000:
      start = time.time()
      ans = solve2(L,m)
      end = time.time()
      print(L,ans,end-start)
      L += 1 

  print "**************"
  print m
  print "runtime: " + str(end-start) + " seconds"


  

  



