"""
Problem Link : https://www.hackerrank.com/challenges/abbr/problem
You can perform the following operation on some string, :

1. Capitalize zero or more of 's lowercase letters at some index i
   (i.e., make them uppercase).
2. Delete all of the remaining lowercase letters in .

Example:
a=daBcd and b="ABC"
daBcd -> capitalize a and c(dABCd) -> remove d (ABC)
"""

def need_transform(first_input: str, second_input: str) -> bool:
    """
    Determines if string first_input can be transformed into string second_input by capitalizing
    zero or more lowercase letters and deleting all other lowercase letters.

    Args:
    first_input (str): The original string.
    second_input (str): The target string.

    Returns:
    bool: True if first_input can be transformed into second_input, False otherwise.
    """

    dp = [[False] * (len(first_input) + 1) for _ in range(len(second_input) + 1)]
    dp[0][0] = True

    for i in range(len(second_input)):
        for j in range(len(first_input) + 1):
            if dp[i][j]:
                if j < len(first_input) and first_input[i].upper() == second_input[j]:
                    dp[i + 1][j + 1] = True
                if first_input[i].islower():
                    dp[i + 1][j] = True

    return dp[len(second_input)][len(first_input)]

print(need_transform("daBcd", "ABC"))