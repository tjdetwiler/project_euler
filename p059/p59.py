


def read_file(file_path):
    with open(file_path) as fp:
      data = fp.read()
    return data


def decode(key,nums):
    ascii_offset = 96
    K = [key[0],key[1],key[2]]
    j = 0 
    dc = ""
    for i in range(0,len(nums)):
        y = int(nums[i])^K[j]
        dc += chr(y)
        j = (j+1) % 3
    return dc


def initial_scan(nums):
    ascii_offset = 96
    
    for a in range(1+ascii_offset,27+ascii_offset):
        print "a = " + str(a)
        for b in range(1+ascii_offset,27+ascii_offset):
            for c in range(1+ascii_offset,27+ascii_offset):
                K = [a,b,c]
                j = 0 
                dc = ""
                for i in range(0,len(nums)):
                    y = int(nums[i])^K[j]
                    dc += chr(y)
                    j = (j+1) % 3
                result1 = dc.find("the")
                result2 = dc.find("and")
                if result1 > -1 and result2 > -1:
                   print (a,b,c)
                   print dc
                   print (result1,result2)
                   print "******************************"




if __name__== "__main__":
    file_path = "cipher1.txt"
    nums = read_file(file_path)
    nums = nums.split(",")
    # used this initial_initial scan to find some likely candidates 
    # for the key

    # initial_scan(nums)

    # from this this 3 character encryption key was found to be the 
    # ascii decimals values [a,b,c] = [103,111,100]
   
    a = 103
    b = 111
    c = 100
    key = [a,b,c]
    msg = decode(key,nums)
    sum = 0
    for m in msg:
        sum += ord(m)
    print msg
    print "************************"
    print sum

