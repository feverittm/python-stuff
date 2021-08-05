def numeric_range(n):
    #print n
    if len(n) == 0:
        #print 0
        return 0
    small=n[0]
    big=n[0]
    for i in n:
        if i < small:
            small=i
        if i > big:
            big=i
    #print small, " ", big, " = ",big-small
    return big-small
    
numeric_range([10, 8, 7, 5, 3, 6, 2])
numeric_range([1, 2, 3])
numeric_range([4])
numeric_range([])
