
# what is fibonacci series?

# a series of numbers in which each number ( Fibonacci number ) is the sum of the two preceding numbers.
# The simplest is the series 1, 1, 2, 3, 5, 8, etc.


# here's the first solution,
def fibonacci_first(nTimes):
    if nTimes == 1: return 1
    elif nTimes == 2: return 2
    else: return fibonacci_first(nTimes-1) + fibonacci_first(nTimes-2)

# def p_test():
#     fibonacci_first(10)
# I hope if you read the above code, it's understable.
# But the problem comes when nTimes value is more than 30, it's taking more time to complete if nTimes is 50

# myCode = '''
# def fibonacci_first(nTimes):
#     if nTimes == 1: return 1
#     elif nTimes == 2: return 2
#     else: return fibonacci_first(nTimes-1) + fibonacci_first(nTimes-2)
# '''
#
# import timeit
# # print(timeit.timeit(setup='', stmt=myCode, number=1000))
# t = timeit.timeit("p_test()")
# # t.timeit(1)


# here's the second solution

fib_cache = {}
def fibonacci_second(numberOfTimes):
    if numberOfTimes in fib_cache:
        return fib_cache[numberOfTimes]

    if numberOfTimes == 1:
        value = 1
    elif numberOfTimes == 2:
        value = 2
    else:
        value = fibonacci_second(numberOfTimes - 1) + fibonacci_second(numberOfTimes - 2)
    fib_cache[numberOfTimes] = value
    return value

# myCode = '''
# fib_cache = {}
# def fibonacci_second(numberOfTimes):
#     if numberOfTimes in fib_cache:
#         return fib_cache[numberOfTimes]
#
#     if numberOfTimes == 1:
#         value = 1
#     elif numberOfTimes == 2:
#         value = 2
#     else:
#         value = fibonacci_second(numberOfTimes - 1) + fibonacci_second(numberOfTimes - 2)
#     fib_cache[numberOfTimes] = value
#     return value'''

# print("So total execution time is, ", timeit.timeit(setup='', stmt=myCode, number=1000))


# Here's the third solution..

from functools import lru_cache

@lru_cache(maxsize=1000)
def fibbonacci_third(nTimes):
    if nTimes == 1:
        return 1
    elif nTimes == 2:
        return 2
    else:
        return fibbonacci_third(nTimes - 1) + fibbonacci_third(nTimes - 2)


for i in range(1, 30):
    print(i , ":" , fibonacci_first(i))

for i in range(1, 151):
    print(i , ":" , fibonacci_second(i))

for i in range(1, 151):
    print(i , ":" , fibbonacci_third(i))