from __future__ import annotations
import sys


def fibonacci(n: int) -> int:
    """
    return F(n)
    >>> [fibonacci(i) for i in range(13)]
    [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]
    """
    if n < 0:
        raise ValueError("Negative arguments are not supported")
    return _privateFibonacci(n)[0]


# returns (F(n), F(n-1))
def _privateFibonacci(userGivenNumber: int) -> tuple[int, int]:
    if userGivenNumber == 0:  # (F(0), F(1))
        return (0, 1)

    # F(2n) = F(n)[2F(n+1) - F(n)]
    # F(2n+1) = F(n+1)^2+F(n)^2
    a, b = _privateFibonacci(userGivenNumber // 2)

    c = a * (b * 2 - a)
    d = a * a + b * b
    
    if n%2:
        return (d, c+d)
    else:
        return (c, d)    


if __name__ == "__main__":
    n = 5
    print(f"fibonacci({n}) is {fibonacci(n)}")