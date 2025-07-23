"""
What is a lambda function in Python?

A lambda function is a small anonymous function defined with the 'lambda' keyword.
It can take any number of arguments but can only have one expression.

Syntax:
    lambda arguments: expression
"""

# Example 1: Basic lambda function
add = lambda x, y: x + y
print("add(2, 3):", add(2, 3))  # Output: 5

# Example 2: Lambda with map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared)  # Output: [1, 4, 9, 16]

# Example 3: Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)  # Output: [2, 4]

# Example 4: Lambda with sorted
pairs = [(2, 3), (1, 4), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
print("Pairs sorted by second element:", sorted_pairs)  # Output: [(5, 0), (2, 3), (1, 4)]

# Comparison: Regular function vs lambda
def multiply(x, y):
    return x * y

multiply_lambda = lambda x, y: x * y

print("multiply(3, 4):", multiply(3, 4))           # Output: 12
print("multiply_lambda(3, 4):", multiply_lambda(3, 4))  # Output: 12

# Note: Lambda functions are best for short, simple operations.