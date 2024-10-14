


sen = "8=FIX.4.2 9=166 35=j 49=broker 56=buySide 34=11 52=20100622-04:56:07 45=12 372=D 379=Order2 380=4 58=MissingDataException: Missing field. Type 50 10=070"

import sys

totalN = len(sys.argv)


for i in range(1,totalN):
    print("Hey arguments passed by user", sys.argv[i])
