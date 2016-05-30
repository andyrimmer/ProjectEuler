
from math import sqrt

###################################################################################################

def isPerfectNumber(x):
    """
    Return 0 if x is perfect, 1 if x is abundant, and -1 if x is
    deficient.
    """
    divisors = set()

    for i in xrange(1, int(sqrt(x)+1)):
        if x % i == 0:
            divisors.add(i)

            if i != 1:
                divisors.add(x/i)

    theSum = sum(divisors)

    if theSum < x:
        return -1
    elif theSum > x:
        return 1
    else:
        return 0

###################################################################################################

abundantNumbers = []
allSums = set()

for x in xrange(1, 28123):
    if isPerfectNumber(x) == 1:
        abundantNumbers.append(x)

print "There are %s abundant numbers" %(len(abundantNumbers))

for x in abundantNumbers:
    for y in abundantNumbers:
        allSums.add(x+y)

print "There are %s sums" %(len(allSums))

theSum = 0

for x in xrange(1, 28123 + 1):
    if x not in allSums:
        theSum += x

print "The sum = %s" %(theSum)
