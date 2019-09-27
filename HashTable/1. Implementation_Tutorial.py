
# CONSTRUCT A HASH TABLE
# ------------------------

single_hash_table = [None] * 10
print(single_hash_table)

# Output:
# [None, None, None, None, None, None, None, None, None, None]

# Below is a simple hash function that returns the modulus of the length of the hash table.
# In our case, the length of the hash table is 10.

# (Modulo operator (%) is used in the hashing function. The % (modulo) operator yields the remainder from the division
# of the first argument by the second.)


def hashing_func(key):
    return key % len(hash_table)


def insert(hash_table, key, value):
    hash_key = hashing_func(key)
    hash_table[hash_key] = value


insert(single_hash_table, 10, 'Nepal')
print(single_hash_table)
# Output:
# ['Nepal', None, None, None, None, None, None, None, None, None]

insert(single_hash_table, 25, 'USA')
print(single_hash_table)
# Output:
# ['Nepal', None, None, None, None, 'USA', None, None, None, None]


# WE HAVE A PROBLEM, "Collision"
# A collision occurs when two items/values get the same slot/index, i.e.
# the hashing function generates same slot number for multiple items.
# If proper collision resolution steps are not taken then the previous item in the slot will be replaced by the
# new item whenever the collision occurs.

# TO RESOLVE ABOVE COLLISION PROBLEM, WE HAVE TWO TYPES

# 1. LINEAR PROBING
# 2. CHAINING


# ####### NEEDS UPDATE #####
