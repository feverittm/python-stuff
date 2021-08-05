from itertools import tee, chain

def with_previous(n, fillvalue=None):
    p = fillvalue
    for x in n:
        yield tuple((x, p))
        p = x

def with_previous_2(n):
    lst = []
    p = None
    for x in n:
        lst.append(tuple((x, p)))
        p = x
        #print x,": p=",p, ", lst=",lst
    return lst

def with_previous_1(n):
    """
    >>> with_previous("hello")
    [('h', None), ('e', 'h'), ('l', 'e'), ('l', 'l'), ('o', 'l')]
    >>> with_previous([1, 2, 3])
    [(1, None), (2, 1), (3, 2)]
    """

    prev = None
    lst = []
    for x in range(0, len(n)):
        if x != 0:
            prev = n[x-1]
        lst.append(tuple((n[x], prev)))

    return lst

