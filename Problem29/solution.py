import itertools

all_powers = sorted([a**b for a,b in itertools.product(range(2,101),
                                                        range(2,101))])

print "Number of unique values = {}".format(len(set(all_powers)))
