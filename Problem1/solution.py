
theSum = 0

for i in xrange(1000):
    if i % 5 == 0:
        theSum += i
    elif i % 3 == 0:
        theSum += i
    else:
        pass

print theSum
