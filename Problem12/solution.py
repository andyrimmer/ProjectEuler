from math import sqrt

triangularNum = 0

for i in xrange(1,10000000):

    triangularNum += i
    factors = set()

    for j in xrange(1, int(sqrt(triangularNum))):

        if triangularNum % j == 0:
            factors.add(j)
            factors.add(triangularNum/j)

    if len(factors) > 500:
        print triangularNum, len(factors)
