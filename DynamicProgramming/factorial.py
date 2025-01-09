
# The @lru_cache is a decorator provided by the functools module in Python. 
# It stands for "Least Recently Used cache". This decorator is used to cache 
# the results of function calls, so that if the function is called again with
#  the same arguments, the cached result is returned instead of recomputing 
# the result. This can significantly improve the performance of functions that
#  are called frequently with the same arguments, especially recursive 
# functions like your factorial function.

# Here's a brief explanation of how it works in your code:

# Caching: When factorial is called with a particular argument, 
# the result is stored in a cache.

# Reuse: If factorial is called again with the same argument, 
# the cached result is returned immediately, avoiding the need for 
# recalculating the factorial.

# Efficiency: This reduces the number of recursive calls and improves the 
# performance of the function.

# To use @lru_cache, you need to import it from the functools module. 
# Here is your updated code with the necessary import statement:

# Factorial of a number using memoization

from functools import lru_cache


@lru_cache
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Number should not be negative.")

    return 1 if num in (0, 1) else num * factorial(num - 1)


if __name__ == "__main__":
    sample_input = 10
    print(factorial(sample_input))