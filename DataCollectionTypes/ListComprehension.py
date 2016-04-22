__author__ = 'Sanjay'
# Let's learn about list comprehensions! You are given three integers X,YX,Y and ZZ representing the dimensions of a cuboid. You have to print a list of all possible coordinates on a 3D grid where the sum of XXii ++ YYii ++ ZZii is not equal to NN. If X=2X=2, the possible values of XXii can be 00, 11 and 22. The same applies to YY and ZZ.
# Input Format

# Four integers X,Y,ZX,Y,Z and NN each on four separate lines, respectively.

# Output Format
# Print the list in lexicographic increasing order.

# Sample Input

# 1
# 1
# 1
# 2
# Sample Output

# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

x, y, z, n = int(input()), int(input()), int(input()), int(input())
print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])