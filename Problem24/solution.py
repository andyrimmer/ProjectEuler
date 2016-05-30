"""
Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
Find the largest index l such that a[k] < a[l].
Swap the value of a[k] with that of a[l].
Reverse the sequence from a[k + 1] up to and including the final element a[n].
"""

###################################################################################################

def permutations(items):
    """
    Permute the elements of 'items' in place, giving the next
    permutation in lexicographic order.
    """
    items = "".join(sorted(items))
    yield items

    while True:
        k = -1
        l = -1
        nItems = len(items)

        for i in xrange(nItems-1):
            if items[i] < items[i+1]:
                k = i

        if k == -1:
            raise StopIteration

        for i in xrange(k, nItems):
            if items[k] < items[i]:
                l = i

        if k == -1 or l == -1:
            raise StopIteration
        else:
            newItems = list(items)
            temp = newItems[k]
            newItems[k] = newItems[l]
            newItems[l] = temp
            items = "".join(newItems)

        items = items[0:k+1] + "".join(reversed(items[k+1:]))
        yield items

###################################################################################################

for index,p in enumerate(permutations("0123456789")):
    if index == 999999:
        print p
        break
