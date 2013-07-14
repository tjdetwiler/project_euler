import sys
import time


def print_sequence(L,P):
    return
    out = ['['] + [' ']*L + [']']
    for (next_tile_index,tile_length) in P:
        for i in range(0,tile_length):
            out[next_tile_index+i+1]=unichr(9724)
    print "".join(out)



def tile_count(L,index,P):
    if index >= L :
        return 0
    min_tile_length = 2
    blue_tile_length = 4
    Porig = P
    count = 0
    while index <= L-2:
        max_tile_length = min(L-index,blue_tile_length)
        for tile_length in range(min_tile_length,max_tile_length+1):
            count +=1
            P = Porig + [(index,tile_length)]
            print_sequence(L,P)
            count += tile_count(L,index+tile_length,P)
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
def solve2(L):
    count = 1
    print_sequence(L,[])
    count += tile_count(L,0,[])
    return count


def solve(L):
    last_diffs = [100,52,27,14]
    last_val = 208
    l = 10
    while l <= L:
        val = last_val + sum(last_diffs)
        # print (l,val,last_val,last_diffs)
        prev_sum = sum(last_diffs)
        last_diffs[3] = last_diffs[2]
        last_diffs[2] = last_diffs[1]
        last_diffs[1] = last_diffs[0]
        last_diffs[0] = prev_sum
        l += 1
        last_val = val
    return val


        


if __name__== "__main__":
  L = 50
  start = time.time()
  ans = solve(L) 
  end = time.time()
  print "*******************"
  print ans
  print "runtime: " + str(end-start) + " seconds"





  



