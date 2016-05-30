"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 = 0.5
1/3 = 0.(3)
...
1/7 = 0.(142857)
...

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
from __future__ import division
from decimal import *
import operator

getcontext().prec = 100

###################################################################################################

def findRepeatingUnit(numerator, denominator):
    """
    Find and return the repeating unit, if it exists,
    in the decimal representation of this fraction.
    """
    frac = Decimal(numerator)/Decimal(denominator)
    strFrac = str(frac)
    lenFrac = len(strFrac)
    maxRepeat = None

    for repeatLen in xrange(1, lenFrac):
        for i in xrange(lenFrac-2*repeatLen):
            if strFrac[i:i+repeatLen] == strFrac[i+repeatLen: i+2*repeatLen]:
                if maxRepeat is None:
                    maxRepeat = strFrac[i:i+repeatLen]
                elif repeatLen > len(maxRepeat):
                    maxRepeat = strFrac[i:i+repeatLen]
                else:
                    pass

    if maxRepeat is None:
        return maxRepeat
    elif len(set(maxRepeat)) == 1:
        return "".join(list(set(maxRepeat)))
    else:
        return maxRepeat

###################################################################################################

repeats = []

for i in xrange(1,1000):
    theRepeat = findRepeatingUnit(1, i)

    if theRepeat is not None:
        repeats.append( (len(theRepeat), theRepeat, i) )

for x in sorted(repeats,key=operator.itemgetter(2)):
    print x
