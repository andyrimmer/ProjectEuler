
x1 = 1
x2 = 2
theSum = 2

for i in xrange(3,1000000):
    new = x1 + x2

    if new >= 4000000:
        break

    if new % 2 == 0:
        theSum += new

    x1 = x2
    x2 = new

print theSum
