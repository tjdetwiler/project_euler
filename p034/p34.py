import imp

#factorials array of 0-9
factorials = [1,1,2,6,24,120,720,5040,40320,362880 ]


def compute_factorial_sum(digits):
    sum = 0
    for d in digits:
        sum += factorials[d]
    return sum

def main():
    utils = imp.load_source("eulerutils","/home/ben/project_euler/problem_solutions/eulerutils.py")

    X = []
    max_val = 10000000
    for i in range(3,max_val):
        digits = utils.get_digits(i)
        x = compute_factorial_sum(digits)
        if x == i:
            X.append(x)
    print X
    print len(X)
    print "***********************"
    print sum(X)



if __name__ == "__main__":
    main()






