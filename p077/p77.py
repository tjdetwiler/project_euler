
def get_primes(max_val):
    vals = list(range(0,max_val+1))
    vals[1] = 0;

    for i in range(2,len(vals)/2 + 2):
      v = vals[i]
      # if v != 0 , then v is prime
      if v == 0:
          continue
      m = 2
      r = m*v

      while r <= max_val:
          vals[r] = 0
          m += 1
          r = m*v
    X = []
    for v in vals:
        if v != 0:
            X.append(v)
    return X

def solve():
    max_val = 100
    count_thresh = 5000
    primes = get_primes(max_val+1)
    S = {}
    counts = {}
    min_val = float('inf')
    iter_count = 0
    current_max_cnt = 0
    current_max_val = float('inf')
    for i in range(0,len(primes)):
        counts[primes[i]] = 1
        S[primes[i]]=[i] 
    while S:
        iter_count += 1
        # print (iter_count,current_max_val,current_max_cnt,len(S))
        Snext = {}
        for val in S:
            indices = S[val] 
            for index in indices:
                for j in range(index,len(primes)):
                    new_val = val+primes[j]
                    if new_val >= min_val:
                        continue
                    if new_val in Snext:
                        Snext[new_val].append(j)
                    else:
                        Snext[new_val] = [j]

                    if new_val in counts:
                        counts[new_val] += 1
                        if counts[new_val] > current_max_cnt:
                            current_max_cnt = counts[new_val]
                            current_max_val = new_val
                        if counts[new_val] > count_thresh:
                            if new_val < min_val:
                                min_val = new_val
                    else:
                        counts[new_val] =  1

                

        
        S = Snext
        do_continue = 0
        for val in S:
            if val < min_val:
                do_continue = 1
                break
        if not do_continue:
            return min_val
             


if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans
