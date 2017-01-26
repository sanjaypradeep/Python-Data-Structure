def square(x):
    return x**2

if __name__ == '__main__':
    print(square(10))

    l1 = [1,2,4,5,654,5,65,778]
    # for i in l1:
    #     print(square(i),end=" ")

    l2 = [None]*len(l1)
    print (l2)

    l3 = (list(map(square, [1,2,4,5,654,5,65,778])))
    l4 = range(len(l1))

    print(dict(zip(l3,l2)))

    from functools import reduce
    # print(list(lambda x,y -> x*y))
    print(list(map(lambda x,y: x*y, l1, l4)))

    # reduce(map(lambda x,y: x+y, [1,2,3,4,5]))

    '''
    [1,2,3,4,5]
    [(1,2),3,4,5]
    [(3),3,4,5] --> [(3,3),4,5]
    [(6),4,5] ---> [(6,4),5]
    [(10),5] --> [(10,5)]
    [15]
    '''

    p = map(lambda x: x*2, [1,2,3,4,5])

    print(list(filter(lambda x: x , list(range(1,11)))))

    print ("hey..")

    def mul(a):
        r = 1
        # for i in a:
        #     r = r * i
        return (r)


    showingToMari = list(map(mul, [1,2,3,4,5]))
    print(showingToMari)

