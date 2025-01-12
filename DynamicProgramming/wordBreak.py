"""
Task:
Given a string and a list of words, return true if the string can be
segmented into a space-separated sequence of one or more words.

Note that the same word may be reused
multiple times in the segmentation.

Implementation notes: Trie + Dynamic programming up -> down.
The Trie will be used to store the words. It will be useful for scanning
available words for the current position in the string.

Leetcode:
https://leetcode.com/problems/word-break/description/

Runtime: O(n * n)
Space: O(n)
"""

import functools
from typing import Any


def word_break(givenInputString: str, words: list[str]) -> bool:
    """
    Return True if numbers have opposite signs False otherwise.

    >>> word_break("applepenapple", ["apple","pen"])
    True
    >>> word_break("catsandog", ["cats","dog","sand","and","cat"])
    False
    >>> word_break("cars", ["car","ca","rs"])
    True
    >>> word_break('abc', [])
    False
    >>> word_break(123, ['a'])
    Traceback (most recent call last):
        ...
    ValueError: the string should be not empty string
    >>> word_break('', ['a'])
    Traceback (most recent call last):
        ...
    ValueError: the string should be not empty string
    >>> word_break('abc', [123])
    Traceback (most recent call last):
        ...
    ValueError: the words should be a list of non-empty strings
    >>> word_break('abc', [''])
    Traceback (most recent call last):
        ...
    ValueError: the words should be a list of non-empty strings
    """
    
    if not isinstance(givenInputString, str) or len(givenInputString) == 0:
        raise ValueError("the string should be not empty string")

    if not isinstance(words, list) or not all(
        isinstance(item, str) and len(item) > 0 for item in words
    ):
        raise ValueError("the words should be a list of non-empty strings")

    word_keeper_key = "WORD_KEEPER"

    
    def build_trie(words: list[str]) -> dict[str, Any]:
        """
        Builds a trie (prefix tree) from a list of words.
        Args:
            words (list[str]): A list of words to be inserted into the trie.
        Returns:
            dict[str, Any]: The root of the trie data structure.
        Example:
            >>> words = ["apple", "app", "banana"]
            >>> trie = build_trie(words)
            >>> print(trie)
            {'a': {'p': {'p': {'l': {'e': {'word_keeper_key': True}}, 'word_keeper_key': True}}}, 'b': {'a': {'n': {'a': {'n': {'a': {'word_keeper_key': True}}}}}}}
        """
        
        trie: dict[str, Any] = {}        

        for word in words:
            trie_node = trie            
            for c in word:
                if c not in trie_node:
                    trie_node[c] = {}
                trie_node = trie_node[c]
            trie_node[word_keeper_key] = True

        return trie
    
        
    """
    The functools.cache decorator is used to cache the results of the function it decorates. This means that when the function is called with the same arguments, the cached result is returned instead of recomputing the result. This can significantly improve performance, especially for recursive functions like is_breakable in your code.

    In your word_break function, functools.cache is used to cache the results of the is_breakable function. This helps avoid redundant calculations and speeds up the process of checking if the string can be segmented into words from the given list.

    Here's a brief explanation of how it works in your code:

    When is_breakable is called with a specific index, the result is computed and stored in the cache.
    If is_breakable is called again with the same index, the cached result is returned immediately, avoiding the need to recompute the result.
    This caching mechanism helps optimize the recursive calls, making the function more efficient.
    """    
    @functools.cache
    def is_breakable(index: int) -> bool:
        
        if index == len(givenInputString):
            return True

        trie_node =  build_trie(words)
        for letter in range(index, len(givenInputString)):
            trie_node = trie_node.get(givenInputString[letter], None)

            if trie_node is None:
                return False

            if trie_node.get(word_keeper_key, False) and is_breakable(letter + 1):
                return True

        return False

    return is_breakable(0)


if __name__ == "__main__":
    print(word_break("applepenapple", ["apple", "pen"]))