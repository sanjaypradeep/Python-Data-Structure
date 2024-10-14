from itertools import repeat
lots_of_fours = repeat(4, times=100000)

print(lots_of_fours)

print(type(lots_of_fours))

# print(list(lots_of_fours))

# This iterator takes up 56 bytes of memory on my machine:

import sys
sys.getsizeof(lots_of_fours)
# 56
# An equivalent list of 100 million 4’s takes up many megabytes of memory:

lots_of_fours = [4] * 100_000_000
import sys
sys.getsizeof(lots_of_fours)

# 800000064
# While iterators can save memory, they can also save time. For example if you wanted to print out just the first line of a 10 gigabyte log file, you could do this:

print(next(open('giant_log_file.txt')))
# This is the first line in a giant file
# File objects in Python are implemented as iterators. As you loop over a file, data is read into memory one line at a time. If we instead used the readlines method to store all lines in memory, we might run out of system memory.

# So iterators can save us memory, but iterators can sometimes save us time also.

# Additionally, iterators have abilities that other iterables don’t. For example, the laziness of iterables can be used to make iterables that have an unknown length. In fact, you can even make infinitely long iterators.