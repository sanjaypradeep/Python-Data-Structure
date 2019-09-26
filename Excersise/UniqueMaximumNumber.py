__author__ = 'Sanjay'

def testing(args):
    uniq = []
    for i in args:
        if args.count(i) == 1:
            uniq.append(i)
    if len(uniq) != 0:
        print max(uniq)
    else:
        print "It seems, all the numbers are repeated!"

if __name__ == '__main__':
    a=int(input())
    b = list(raw_input())
    while True:
        try:
            b.remove(" ")
        except ValueError:
            break
    orgInput = []
    for i in b:
        if i != '':
            orgInput.append(int(i))
        else:
            pass
    print orgInput
    testing(orgInput)