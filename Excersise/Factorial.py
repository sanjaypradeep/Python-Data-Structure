def fac(givenInput):
    if givenInput>1:
        i = range(1, givenInput+1)
        op = 1
        for m in i[::-1]:
            op = op * m
    print (op)

if __name__ == '__main__':
    inputForFactorial = int(input("Enter a number! I will you the factorial results."))
    fac(abs(inputForFactorial))