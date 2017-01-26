__author__ = 'Sanjay'
"""
Himanshu and Luck
Max. Marks 100
Himanshu and Luck
Himanshu is quite a lucky person, or atleast he claims to be. Recently, he has started some research work in college and guess what is he researching on? Lucky Numbers! While doing his bit of research, a fellow colleague of him asked him a pretty awkward question : "Given a range as input, find the number of lucky numbers lying in that range!". Himanshu somehow solved this problem, but now he has a bigger challenge for you : "There are Q queries, each of which contains a range. Find out the number of lucky numbers lying in each range (inclusive of end points)." Are you up for this hack?
Note : A number is a lucky number if it contains 4 or 7, or both in its decimal representation.
Examples:
1) 147 is not a Lucky Number as it contains 1 as an extra element, which violates the property of Lucky Numbers.
2) 47, 44, 77 , 447, 774, 4, 7 are the examples of Lucky number.
Input Format
First line contains T, the number of test cases. Each of the next T lines contains two space separated integers L and R, depicting the range.
Output Format
For each of the T lines, output one integer : The answer as specified.
Constraints
1 <= T <= 10000
1 <= L <= R <= 10^18

Sample Input
(Plaintext Link)
3
1 4
2 3
1 1
Sample Output
(Plaintext Link)
1
0
0
Explanation
a) Between 1 and 4, there is only 1 Lucky number, i.e 4.
b) Between 2 and 3, there are no Lucky Numbers.
c) Between 1 and 1, there are no Lucky Numbers.

Time Limit: 1 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed languages: C, CPP, CLOJURE, CSHARP, GO, HASKELL, JAVA, JAVASCRIPT, JAVASCRIPT_NODE, LISP, OBJECTIVEC, PASCAL, PERL, PHP, PYTHON, RUBY, R, RUST, SCALA
"""

sDigitLuckNum1 = 4
sDigitLuckNum2 = 7

dDigitLuckNum1 = "44"
dDigitLuckNum2 = "47"
dDigitLuckNum3 = "74"
dDigitLuckNum4 = "77"

tDigitLuckNum1 = "444"
tDigitLuckNum2 = "447"
tDigitLuckNum3 = "477"
tDigitLuckNum4 = "777"
tDigitLuckNum5 = "774"
tDigitLuckNum6 = "744"

def someMethod():

    totalCase = input()
    userInput = []
    for i in range(int(totalCase)):
        a, b = input().split(" ")
        userInput.append([int(a), int(b)])

    for i in userInput:
        answer = 0
        for element in i:
            if len(str(element)) > 2:
                numberOfFours = list(str(element)).count(str(sDigitLuckNum1))
                numberOfSevens = list(str(element)).count(str(sDigitLuckNum2))
                if (numberOfFours+numberOfSevens == len(str(element))):
                    answer += len(str(element))
                else:
                    pass
            if len(str(element)) == 2 and (str(element).__contains__(dDigitLuckNum1) or
                                               str(element).__contains__(dDigitLuckNum2) or
                                               str(element).__contains__(dDigitLuckNum3)or
                                                str(element).__contains__(dDigitLuckNum4)):
                answer += 2
            if len(str(element)) == 1 and (element is sDigitLuckNum1 or element is sDigitLuckNum2):
                answer += 1
        print (answer)

# Now the above implementation accepts the user input as Single and Double Digits.
# As mentioned in the previous commit, now two digits input are accepted. Implementation is done.
# (As mentioned in old commit) Final done!! Accepting 3 or more digits inputs from user, tested in different scenarios. DONE

if __name__ == '__main__':
    someMethod()