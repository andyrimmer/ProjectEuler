from math import sqrt

###################################################################################################

def primes():
    i = 0
    while True:
        i += 1

        if i == 0 or i == 1:
            continue
        elif i == 2:
            yield i
        else:
            for j in xrange(2, int(sqrt(i)+0.5)+1):
                if i % j == 0:
                    break
            else:
                yield i

###################################################################################################

def isPrime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for j in xrange(2, int(sqrt(x)+0.5)+1):
            if x % j == 0:
                return False
        else:
            return True

###################################################################################################

testNumber = 600851475143
biggest = 0

#for index,p in enumerate(primes()):
#    if testNumber % p == 0:
#        biggest = p
#        print biggest
#
#    if index % 5000 == 0:
#        print "Tried %s prime numbers. Got to %s. Biggest factor is %s" %(index+1, p, biggest)


for i in xrange(2,int(sqrt(testNumber))):

    if testNumber % i == 0:
        x = testNumber / i

        if isPrime(x):
            biggest = max(x, biggest)
            print "Found prime factor %s." %(x)

        if isPrime(i):
            biggest = max(i, biggest)
            print "Found prime factor %s." %(i)

print "Biggest prime factor = %s" %(biggest)
