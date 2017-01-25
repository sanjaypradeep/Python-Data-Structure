


l1 = range(10)

l2 = range(5)

if len(l1) != len(l2):
    diff = abs(len(l1) - len(l2))
    if len(l1) >= len(l2):
        for i in range(diff):
            l2.append(None)
        print l2
        d1 = zip(l1,l2)
        print dict(d1)
else:
    pass