__author__ = 'Sanjay'

"""
Navi and beer
Max. Marks 100
Navi and beer
Navi is at the Beer Bar where he has ordered N beers. After seeing his love with the beers, Bar's Manager has decided to make as much money as they can by asking Navi to pay K * i3 Rupees for the ith beer. But Navi has only M Rupees in his purse. So you are required to lent him some money so that he can still be able to pay for all of the N beers.
Input:
First line will contain T (No. of test cases).
Each test case will contain only one line having three space separated integers : N, K and M
Output:
For every test case, print the required answer in a new line.
Constraints:
1 ? T ? 105
1 ? N, K ? 103
1 ? M ? 106
Sample Code:
  #include <iostream>
    using namespace std;

    int main()
    {
        //taking input for number of test cases, T.
        cin>>T;

        //For every test case, taking input for N , K and M.
        cin>>N>>K>>M;

        //let the answer be in variable **Ans**
        cout << Ans << endl; //print your answer for every test case.
        return 0;
    }

Sample Input
(Plaintext Link)
1
2 2 10
Sample Output
(Plaintext Link)
8
Explanation
Total Money required is : 2 * 13 + 2 * 23 = 18 but he already has 10 so ans is 8.

Time Limit: 1 sec(s) for each input file.
Memory Limit: 256 MB
Source Limit: 1024 KB
Marking Scheme: Marks are awarded if any testcase passes.
Allowed languages: C, CPP, CLOJURE, CSHARP, GO, HASKELL, JAVA, JAVASCRIPT, JAVASCRIPT_NODE, LISP, OBJECTIVEC, PASCAL, PERL, PHP, PYTHON, RUBY, R, RUST, SCALA
"""

def remaingAmount(numberOfBeers,eachBeerCost,rupeesInPurse):
    totalCost1 = 0
    totalCost2 = 0
    for i in range(eachBeerCost):
        if i == 0:
            i = 1
            totalCost1 = numberOfBeers * i**3
        else:
            i = i+1
            totalCost2 = numberOfBeers * i**3

        finalCost = totalCost1 + totalCost2
    remaingBalance = finalCost - rupeesInPurse
    print (abs(remaingBalance))


if __name__ == '__main__':
    remaingAmount(2,2,10)

#
# class A():
#     print ("sanjay")
#     def __init__(self):
#         print ("s")
#
# x = A()
# print (x)
#
# print ([i for i in range(5) if i%3 ==0 ])