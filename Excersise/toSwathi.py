
def splitInputsByCategory(bigList, conditionList):
    x_neg = []
    x_pos = []
    for i in conditionList:
        if i == 0:
            x_neg.append(bigList[0])
            del x[0]
        elif i == 1:
            x_pos.append(bigList[0])
            del x[0]
    return x_pos,x_neg

if __name__ == '__main__':
    x = [
        [1, -0.8, 0.832],
        [1, 0.3571, 0.85090],
        [1, -0.75, -0.74343],
        [1, -0.3, 0.12545],
        [1, 0.83465567, 0.62434554],
        [1, -0.02, 0.9200034354],
        [1, 0.104365545, -0.3243566757],
        [1, 0.00007143, 0.073278437e3],
    ]
    y = [0,0,0,0,1,1,1,1]
    xPos, xNeg = splitInputsByCategory(x, y)
    print (xPos)
    print (xNeg)


