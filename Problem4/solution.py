
biggest = 0

for x in xrange(100, 1000):
    for y in xrange(100, 1000):
        product = x*y
        reverseProduct = int("".join([i for i in reversed(str(product))]))

        if product == reverseProduct:
            biggest = max(biggest, product)

print "Biggest = ", biggest
