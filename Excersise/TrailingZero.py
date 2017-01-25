__author__ = 'Sanjay'


def trails(n):
    listOfMultiples = [5,25,125,625,3125,15625]

    ans = 0
    if n > 1:
        for i in listOfMultiples:
            cal = n/i
            if cal < 1:
                break
            else:
                ans = ans + cal
        print ans


if __name__ == '__main__':
    trails(999)
