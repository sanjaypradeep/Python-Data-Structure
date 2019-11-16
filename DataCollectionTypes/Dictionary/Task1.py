

globalKeys = []
globalValues = []

GLOBAL_FILENAME = "input1.txt"
GLOBAL_FILE_PERMISSION = "w+"


def iterateListFunction(args):
    '''
    args : takes arguments as list.
    desc : separates key and value from dict/json.
    '''
    for i in args:
        if type(i) == dict:
        globalKeys.append(*i)
        globalValues.append(list(i.values()))


def appendingAllElementsInAList(alist):
    '''
    args : takes arguments as list.
    desc : separates key and value from dict/json accordingly.
    '''
    finalOutput = []
    for i in alist:
        if type(i) == list:
            for z in i:
                finalOutput.append(z)
        else:
            finalOutput.append(i)
    return finalOutput

def writeFinalOutput(manipulatedOutput):
    '''
    args : manipulatedOutput - separated out as list (which is internally a zip object).
    desc : Writes the output to the text file.
    '''
    outF = open(GLOBAL_FILENAME, GLOBAL_FILE_PERMISSION)
    outF.write("Keys    Values")
    outF.write("\n")
    for line in manipulatedOutput:
        # write line to output file
        outF.write(line[0] + "\t\t\t" + str(line[1]))
        outF.write("\n")
    outF.close()
    print("Program executed successfully! Please verify output at input1.txt")

if __name__ == '__main__':

    userGivenInput = { 'a':  
                [ 
                    { 'h':  'e' }, 
                    { 'f':  'r' }, 
                    { 
                        't':  [ 'w', 'x' ] 
                    } 
                ] ,
                    'b':  [
                            {
                                    'P':  [ 'd', 'c' ] 
                            }, 
                            {
                                'l': 'q' 
                            } 
                        ]
                }

    for k,v in userGivenInput.items():
        if type(v) == list:
            iterateListFunction(v)
                 
        finalValueOutput = []

        for i in globalValues:
            if type(i) == list:
                for j in i:
                    finalValueOutput.append(j)
    opKeys = appendingAllElementsInAList(list(globalKeys))
    opValues = appendingAllElementsInAList(globalValues)

    finalOp = list(zip(opKeys, opValues))

    writeFinalOutput(finalOp)