###################################################################################################

numbers = {}
numbers[0] = ""
numbers[1] = "one"
numbers[2] = "two"
numbers[3] = "three"
numbers[4] = "four"
numbers[5] = "five"
numbers[6] = "six"
numbers[7] = "seven"
numbers[8] = "eight"
numbers[9] = "nine"
numbers[10] = "ten"
numbers[11] = "eleven"
numbers[12] = "twelve"
numbers[13] = "thirteen"
numbers[14] = "fourteen"
numbers[15] = "fifteen"
numbers[16] = "sixteen"
numbers[17] = "seventeen"
numbers[18] = "eighteen"
numbers[19] = "nineteen"
numbers[20] = "twenty"
numbers[30] = "thirty"
numbers[40] = "forty"
numbers[50] = "fifty"
numbers[60] = "sixty"
numbers[70] = "seventy"
numbers[80] = "eighty"
numbers[90] = "ninety"
numbers[100] = "hundred"
numbers[1000] = "onethousand"

###################################################################################################

def countLetters(x):

    if x > 1000:
        raise StandardError, "?"

    if x == 1000:
        return len(numbers[x])

    theSum = 0

    hundreds = x//100
    remainder = x - hundreds*100
    theSum += len(numbers[hundreds])

    if hundreds > 0:
        theSum += len("hundred")

        if remainder > 0:
            theSum += len("and")

    tens = remainder//10

    if tens == 1:
        theSum += len(numbers[remainder])
    else:
        remainder = remainder - tens*10
        theSum += len(numbers[tens*10])
        theSum += len(numbers[remainder])

    return theSum

###################################################################################################

def makeString(x):

    if x > 1000:
        raise StandardError, "?"

    if x == 1000:
        return numbers[x]

    theStr = ""
    hundreds = x//100
    remainder = x - hundreds*100
    theStr += numbers[hundreds]

    if hundreds > 0:
        theStr += "hundred"

        if remainder > 0:
            theStr += "and"

    tens = remainder//10

    if tens == 1:
        theStr += numbers[remainder]
    else:
        remainder = remainder - tens*10
        theStr += numbers[tens*10]
        theStr += numbers[remainder]

    return theStr

###################################################################################################

#total = sum([countLetters(x) for x in xrange(1,6)])
total = sum([countLetters(x) for x in xrange(1,1001)])

for x in xrange(1,1001):
    print makeString(x)

print total
