from math import sqrt

for x in xrange(1,500):
    for y in xrange(x+1,500):
        root = sqrt(x**2 + y**2)
        if root == int(root) and x + y + root == 1000:
            print x,y,root, x+y+root, x*y*int(root)
        #if x**2 + y**2 == z**2:
