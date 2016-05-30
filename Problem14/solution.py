

###################################################################################################

def collatz(x):
    yield x

    while x != 1:
        if x % 2 == 0:
            x = x/2
            yield x
        else:
            x = 3*x + 1
            yield x

    yield x

###################################################################################################

longest = 0

for i in xrange(1,1000000):
    for index,x in enumerate(collatz(i)):
        if x == 1:
            if index+1 > longest:
                longest = index+1
                print "New longest = %s for %s" %(longest, i)
