from math import sqrt

###################################################################################################

def primes():
    yield 2
    yield 3
    i = 4
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

for i,p in enumerate(primes()):
    if i == 10000:
        print i+1,p
        break
