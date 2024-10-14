
def findActions(s1, s2):
    if len(s1) > len(s2):
        for i in s1:
            print(i[0])
    elif len(s1) < len(s2):
        pass
    else:
        pass

def OneEditApart(s1, s2):
    if type(s1) != str and type(s2) != str:
        return False
    
    if len(s1) == 0 or len(s2) == 0:
        return False

    eS1 = enumerate(s1)
    eS2 = enumerate(s2)

    print(list(eS1))
    print(list(eS2))


OneEditApart("Geeks", "Geek")
print("s")