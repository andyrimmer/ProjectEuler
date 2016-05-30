

def fibonacci():
    n1 = 1
    n2 = 1
    yield n1
    yield n2

    while True:
        newFib = n1 + n2
        yield newFib
        n1 = n2
        n2 = newFib


length = 1

for index,x in enumerate(fibonacci()):
    print x
    #if len(str(x)) >= length:
    #    print length,index + 1
    #    length += 1
