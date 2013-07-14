import itertools

arragements = []
op_set = []

def is_int(x):
    eps = 1e-4
    if abs(x - int(x)) < eps:
        return 1
    return 0


def get_expression_arrangements():
    A = []
    A.append('{0}{4}{1}{5}{2}{6}{3}')
    A.append('{0}{4}({1}{5}({2}{6}{3}))')
    A.append('({0}{4}{1}){5}({2}{6}{3})')
    A.append('(({0}{4}{1}){5}{2}){6}{3}')
    A.append('{0}{4}({1}{5}{2}{6}{3})')
    A.append('({0}{4}{1}{5}{2}){6}{3}')
    A.append('({0}{4}{1}){5}{2}{6}{3}')
    A.append('{0}{4}({1}{5}{2}){6}{3}')
    A.append('{0}{4}{1}{5}({2}{6}{3})')
    A.append('({0}{4}({1}{5}{2})){6}{3}')
    A.append('{0}{4}(({1}{5}{2}){6}{3})')
    return A


def get_operator_sets():
    ops = ['-','+','*','/']
    c = list(itertools.combinations_with_replacement(ops,len(ops)-1))
    X = []
    for cc in c:
        X += list(set(itertools.permutations(cc,len(ops)-1)))
    return X

def get_number_sets(quad):
    quad = [str(q) for q in quad]
    return list(set(itertools.permutations(quad,len(quad))))



def count_consecutive(x):
    x.sort()
    c = 0
    max_consec = 0
    for i in range(1,len(x)):
        if x[i]-x[i-1] == 1:
            c += 1
            if c > max_consec:
                max_consec = c
        else:
            c = 0
    return max_consec

   
    
def analyze_set(quad):
    quads = get_number_sets(quad)
    S = []
    c = 0

    for q in quads:

       for ops in op_set:
           for a in arrangements:
               z = q+ops
               try:
                   expression = a.format(*z)
                   val = eval(expression)

                   if is_int(val):
                       val = int(val)
                       if val >= 0 and val  not in S:
                           # print (expression, val)
                           S.append(val)
               except:
                   continue
    return count_consecutive(S)

def solve():
    global arrangements
    global op_set
    max_count = 0
    arrangements = get_expression_arrangements()
    op_set = get_operator_sets()

    quad = [1.,2.,3.,4.]
    all_nums = [float(n) for n in range(1,10)]
    nums = itertools.combinations(all_nums,4)
    c = 0
    for quad in nums:
        c += 1
        consec_count = analyze_set(quad)
        print (c,quad,consec_count)
        if consec_count > max_count:
            max_count = consec_count
            max_quad = quad
    return (max_count,max_quad)


        
                        
                    
    



if __name__  == "__main__":
    ans = solve()
    print "*************************"
    print ans
