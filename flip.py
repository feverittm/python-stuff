from collections import defaultdict, OrderedDict

def null_func(n):
    return n

def flip_dict_of_lists(n, dict_type=None, key_func = null_func):
    """
    For this exercise I want you to write a function that takes a dictionary of lists and returns a "flipped" dictionary of lists. What I mean by "flipped" is this:
        >>> d = {'a': [1, 2], 'b': [3, 1], 'c': ['2']}
        >>> flip_dict_of_lists(d)
        {1:  ['a', 'b'], 2: ['a', 'c'], 3: ['b']}

        Your function should accept any dictionary type and the output lists should maintain the order of given keys (for ordered dictionaries).
    """
    if dict_type is None:
        flipped = {}
    else:
        flipped = OrderedDict()

    #print n
    for nkey in n.iterkeys():
        for nlist in n[nkey]:
            #print nkey, " ", nlist
            try:
                flipped[key_func(nlist)].append(nkey)
            except:
                flipped[key_func(nlist)] = []
                flipped[key_func(nlist)].append(nkey)
    return flipped


