
#x = 1
#
#for i in xrange(1,11):
#    x *= i
#
#print x

for i in xrange(20,1000000000, 20):
    for n in xrange(1,21):
        if i % n != 0:
            break
    else:
        print i
        break
