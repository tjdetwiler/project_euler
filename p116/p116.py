import sys
import time

def print_outline(L,tile_length,P):
    out = ['['] + [unichr(9633)]*L + [']']
    print "".join(out)

def print_sequence(L,tile_length,P,r=None):
    return
    out = ['['] + [' ']*L + [']']
    for p in P:
        for i in range(0,tile_length):
            index = 1+ p-(tile_length-1)+i

            if index >= len(out)-1:
                print 'error: index ' + str(index) + ' out of bounds'
                print (r,P )
                exit(0)
            out[index]=unichr(9724)
    print "".join(out)



def combo_count(L,tile_length,shift_index,P):
    if shift_index < 0:
        return 0

    tile_count = len(P)

    loc = P[shift_index]
    # print 'P = ' +str(P)

    if tile_count > 1 and shift_index < tile_count -1:
        next_tile_pos = P[shift_index+1]
        max_pos = next_tile_pos-tile_length

    else:
        max_pos = L-1    



    count = 0
    shifts = 1
    Porig = P
    while loc < max_pos:
        count +=1


        nextP = P[:shift_index] + [P[shift_index]+1]+P[shift_index+1:]
        loc = P[shift_index]+1
        print_sequence(L,tile_length,nextP,shift_index)
        # print (shift_index,loc,max_pos,nextP)
        # print ""

        count += combo_count(L,tile_length,shift_index-1,nextP)

        P = nextP


    return count    


def total_combo_count(L,tile_length):
    count = 0
    for tile_count in range(1,L/tile_length+1):
        shift_index= tile_count -1
        P = [(i+1)*tile_length-1 for i in range(0,tile_count)]
        # print_outline(L,tile_length,P)
        # print P        
        print_sequence(L,tile_length,P)
        # print ""
        count += combo_count(L,tile_length,shift_index,P)+1
    return count

def gs(tile_length):
    last = 0
    for L in range(tile_length,21):
        result =  total_combo_count(L,tile_length)
        if L >= tile_length*2:
            print (L,result,result-last)
        # print (L,result,result-last)
        last = result
    return 0

def gs2(tile_length,board_length):
    last_diffs = [1]*tile_length
    L = tile_length * 2
    last = tile_length
    count = board_length - tile_length+1
    while L <= board_length:
        count = last + last_diffs[len(last_diffs)-1] + last_diffs[0]
        diff = count-last
        # print (L,count)
        new_diffs = []
        for i in range(1,len(last_diffs)):
            new_diffs.append(last_diffs[i])
        new_diffs.append(diff)
        last_diffs = new_diffs
        last = count
        L += 1

    return count

def solve2(L):
    count = 0
    for tile_length in [2,3,4]:
        result = gs2(tile_length,L)
        # print (tile_length,result)
        count += result
    return count

def solve(L):
    count = 0
    for tile_length in [2,3,4]:
        result =  total_combo_count(L,tile_length)
        # print (tile_length, result)
        count += result
    return count
        



if __name__== "__main__":
  L =50
  start = time.time()
  ans = solve2(L)
  end = time.time()
  print "**************"
  print ans
  print "runtime: " + str(end-start) + "seconds"
  

  

