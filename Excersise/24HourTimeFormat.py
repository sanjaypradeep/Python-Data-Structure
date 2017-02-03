# https://www.hackerrank.com/challenges/time-conversion

givenTime = input()
timeListFormat = list(givenTime)
hour = []
finalOutput = ''

if "AM" in givenTime:
    # if list(timeListFormat[0:2]) == [1,2]:
    if int(timeListFormat[0]) == 1 and int(timeListFormat[1]) == 2:
        timeListFormat[0] = str(0)
        timeListFormat[1] = str(0)
    for i in timeListFormat[0:8]:
        finalOutput += i
    print(finalOutput)
elif "PM" in givenTime:
    for i in timeListFormat[0:2]:
        hour.append(int(i))

    if int(timeListFormat[0]) == 1 and int(timeListFormat[1]) == 2:
        for i in timeListFormat[0: len(timeListFormat) - 2]:
            finalOutput += i
    else:
        x = ''
        for i in hour:
            x += str(i)
        finalOutput += str(int(x) + 12)
        for i in timeListFormat[2: len(timeListFormat)-2]:
            finalOutput += i

    print (finalOutput)