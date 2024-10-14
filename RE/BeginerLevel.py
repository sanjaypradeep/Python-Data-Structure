'''
Ram, consider this file as beginer level tutorial kinda things.
you will learn about regular expressions (RegEx), and use Python's re module to work with RegEx (with the help of examples).

A Regular Expression (RegEx) is a sequence of characters that defines a search pattern. 

'''
# below line a regex pattern
example_pattern = '^a...s$'

# What can we do with this above pattern?
# What did you understand when you read this pattern?

# Matching Patterns with example.. 

# Expression	String	        Matched
# ^a...s$	        abs	        No match
                # alias	      Match
                # abyss	      Match
                # Alias	      No match
                # An abacus	  No match


# Code Implementation example, 

import re # re is the pre-defined module that exist inside Python

sample_test_string = 'Sanjay is conducting a session to Ram alias prrampalli who is residing in London'
sample_focused_string = "abs"

# example_pattern = '^a...s$'

result = re.match(example_pattern, sample_focused_string)
print(result)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	


# from the above example, we used re.match() to check string match, there're other method under re, those are,
# re.compile
# re.sub
# re.search
# re.findall
# re.split

# To specify regular expressions, metacharacters are used. In the above example, ^ and $ are metacharacters

'''
What is meta characters?

Metacharacters are characters that are interpreted in a special way by a RegEx engine. Here's a list of metacharacters:

[] . ^ $ * + ? {} () \ |

'''

# 1 - We can discuss about []

# Expression	    String	      Matched?
# [abc]	            a	          1 match
#                   ac	        2 matches
#                   Hey Jude	  No match
#                   abc de ca	  5 matches

# [abc] will match if the string you are trying to match contains any of the a, b or c.

# You can also specify a range of characters using - inside square brackets.

# [a-e] is the same as [abcde].
# [1-4] is the same as [1234].
# [0-39] is the same as [01239]. **

# You can complement (invert) the character set by using caret ^ symbol at the start of a square-bracket.

# [^abc] means any character except a or b or c.
# [^0-9] means any non-digit character.



# 2 - We can now discuss about .

'''
. -> called as period

A period matches any single character (except newline '\n').

Expression	    String	    Matched?
..	            a	          No match
                ac	        1 match
                acd	        1 match
                acde	      2 matches (contains 4 characters)
'''

# 3 - We can discuss about Carret.

'''
^ - Caret

The caret symbol ^ is used to check if a string starts with a certain character.

Expression	    String	    Matched?
^a	            a	        1 match
                abc	        1 match
                bac	        No match
^ab	            abc	        1 match
                acb	        No match (starts with a but not followed by b)

'''

#  4 - We can look into $

'''
$ - Dollar

The dollar symbol $ is used to check if a string ends with a certain character.

Expression	    String	    Matched?
a$	            a	          1 match
                formula	    1 match
                cab	        No match
                ram         No Match
                ra          1 Match
'''


# 5 - Astriek or star

'''
* - Star

The star symbol * matches zero or more occurrences of the pattern left to it.

Expression	    String	    Matched?
ma*n	        mn	        1 match
                man	        1 match
                maaan	    1 match
                main	    No match (a is not followed by n)
                woman	    1 match
                ran         No match
                ram         No Match
                maen        No Match
                maaaaaaan   1 Match
'''

# 6 - Plus
'''
+ - Plus

The plus symbol + matches one or more occurrences of the pattern left to it.

Expression	    String	    Matched?
ma+n	        mn	        No match (no a character)
                man	        1 match
                maaan	    1 match
                main	    No match (a is not followed by n)
                woman	    1 match
'''

# 7 - ? - Question Mark
'''
The question mark symbol ? matches zero or one occurrence of the pattern left to it.

Expression	    String	    Matched?
ma?n	        mn	          1 match
                man	        1 match
                maaan	      No match (more than one a character)
                main	      No match (a is not followed by n)
                woman	      1 match
                maon        No match
                exmain      No match 
'''


# 8 - {} - Braces

'''
Consider this code: {n,m}. This means at least n, and at most m repetitions of the pattern left to it.

Expression	    String	    Matched?
[a-z]{2,3}	    abc dat	    No match
                abc daat	  1 match (at daat)
                aabc daaat	2 matches (at aabc and daaat)
                aabc daaaat	2 matches (at aabc and daaaat)
                a           No Match
                aa          1 Match
                aaaaaabb    1 Match

Let's try one more example. This RegEx [0-9]{2, 4} matches at least 2 digits max as 4 digits

Expression	    String	        Matched?
[0-9]{2,4}	    ab123csde	      1 match (match at ab123csde)
                12 and 345673	  3 matches (12, 3456, 73)
                1 and 2	        No match
'''

# 9. | - Alternation
'''
Vertical bar | is used for alternation (or operator).

Expression	    String	    Matched?
a|b	            cde	        No match
                ade	        1 match (match at ade)
                acdbea	    3 matches (at acdbea)

Here, a|b match any string that contains either a or b
'''
# 10 () - Group
'''
Parentheses () is used to group sub-patterns. For example, (a|b|c)xz match any string that matches either a or b or c followed by xz

Expression	String	    Matched?
(a|b|c)xz	    ab xz	    No match
              abxz	    1 match (match at abxz)
              axz cabxz	2 matches (at axzbc cabxz)
'''

# 11. \ - Backslash
'''
Backlash \ is used to escape various characters including all metacharacters. For example,

\$a match if a string contains $ followed by a. Here, $ is not interpreted by a RegEx engine in a special way.

If you are unsure if a character has special meaning or not, you can put \ in front of it. 
This makes sure the character is not treated in a special way.

Special Sequences
-------------------

Special sequences make commonly used patterns easier to write. Here's a list of special sequences:

\A - Matches if the specified characters are at the start of a string.

Expression	    String	                    Matched?
\A              the	the sun	                Match
                In the sun	                No match

\b - Matches if the specified characters are at the beginning or end of a word.

Expression	            String	        Matched?
\bfoo	                football	        Match
                      a football	      Match
                      afootball	        No match

foo\b	                the foo	          Match
                      the afoo test	    Match
                      the afootest	    No match

\B - Opposite of \b. Matches if the specified characters are not at the beginning or end of a word.

Expression	        String	          Matched?
\Bfoo	              football	        No match
                    a football	      No match
                    afootball	        Match

foo\B	              the foo	          No match
                    the afoo test	    No match
                    the afootest	    Match

\d - Matches any decimal digit. Equivalent to [0-9]

Expression	    String	        Matched?
\d	            12abc3	        3 matches (at 12abc3)
                Python	        No match

\D - Matches any non-decimal digit. Equivalent to [^0-9]

Expression	    String	    Matched?
\D	            1ab34"50	3 matches (at 1ab34"50)
                1345	    No match

\s - Matches where a string contains any whitespace character. Equivalent to [ \t\n\r\f\v].

Expression	    String	        Matched?
\s	            Python RegEx	  1 match
                PythonRegEx	    No match

\S - Matches where a string contains any non-whitespace character. Equivalent to [^ \t\n\r\f\v].

Expression	    String	    Matched?
\S	            a b	2       matches (at  a b)
   	                        No match

\w - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.

Expression	    String	    Matched?
\w	            12&": ;c 	  3 matches (at 12&": ;c)
                %"> !	      No match


\W - Matches any non-alphanumeric character. Equivalent to [^a-zA-Z0-9_]

Expression	    String  	Matched?
\W	            1a2%c	    1 match (at 1a2%c)
                Python	  No match

\Z - Matches if the specified characters are at the end of a string.

Expression	    String	                    Matched?
Python\Z	    I like Python	                1 match
              I like Python Programming	    No match
              Python is fun.	              No match

Tip: To build and test regular expressions, you can use RegEx tester tools such as regex101. This tool not only helps you in creating regular expressions, but it also helps you learn it.

Now you understand the basics of RegEx, let's discuss how to use RegEx in your Python code.
'''


# From the above features we went through, here's the list of exercise for you!

# 1. Write a method(giveMeNumber) takes input as string, gives output as available numbers inside the give string.

# Sample,
# givenInput = "hey my phone number starts with 91 as country code, then my 10 digit # continues - 9944294841"

# giveMeNumber(givenInput) #[91, 10, 9944294841]


# 2. 