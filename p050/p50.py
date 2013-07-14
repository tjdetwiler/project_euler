import numpy as np

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


def get_cum_sum(nums):
    sum = 0
    x = []
    for i in nums:
        sum += i
        x.append(sum)
    return x


def get_diff_matrix(nums):
    n = len(nums) - 1
    X = np.zeros((n,n))
    for i in range(0,n):
        for j in range(i+1,n+1):
            X[i,j-1] = nums[i] - nums[j]
    return X         

def get_subset_index(primes,max_val):
    for i in range(0,len(primes)):
        if primes[i] > max_val:
            return i 
    return -1


def main():
    # only use a subset to calcuate the sums
    # because you can assume the largest primes, just 
    # below 1 million won't be used
    subset_max = int(1e5)
    max_val = int(1e6)
    print "finding primes below " + str(max_val)
    primes = get_primes(max_val)
    i = get_subset_index(primes,subset_max)
    print "creating cumulative sum of primes.."
    cs = get_cum_sum(primes)
    print "creating diff matrix.."
    M = get_diff_matrix((cs[:i])[::-1])
    print "finding max prime..."

    c = 0
    lm = len(M)

    while c < lm:
        xs = 0
        ys = lm-1-c
        for i in range(0,c+1):   
            v = M[xs,ys]
            if int(v) < 1000000:
                if v in primes:
                    print "********************"
                    print v
                    return
            xs += 1
            ys += 1

        c += 1
    return -1



if __name__ == "__main__":
    main()
