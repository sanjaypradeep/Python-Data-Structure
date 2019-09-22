# filter() in python
# The filter() method filters the given sequence with the help of a function that tests each element in the sequence to be true or not.

def checkHowManyVowelsDoesYourNameHave(nameAsInput):
    a = list(nameAsInput)
    print(list(a))
    b = list(map(lambda x: x in ['a','e','i','o','u'], a))
    print(b)

    dictOp = {}
    for i in list(nameAsInput):
        if i in ['a','e','i','o','u']:
            dictOp[i] = True

    print(dictOp)


checkHowManyVowelsDoesYourNameHave("Sanjay")


def checkVowels(alInput):
    if alInput in ['a','e','i','o','u']:
        return True
    else:
        return False


sampleSentence = "How many vowels does this sentence have?"

print(set(filter(checkVowels, list(sampleSentence))))