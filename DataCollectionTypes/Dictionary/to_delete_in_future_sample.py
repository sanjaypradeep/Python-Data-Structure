# import pyodbc
# import json

# # reads N number of lines of queries
# def readSQL():
#     with open('queries.sql', 'r') as sqlFile:
#         line = sqlFile.readlines()
#         return line

# def sqlConnect():
#     conn = pyodbc.connect('Driver={SQL Server};'
#                           'Server=DESKTOP-AV96G7N;'
#                           'Database=AdventureWorks2019;'
#                           'Trusted_Connection=yes;')
#     cursor = conn.cursor() 
#     return cursor

# def executeSQLQuery(cursorObj, query):
#     execResult = cursorObj.execute(query)
#     return execResult

# def getCursorData(cursorObj):
#     outputDict = {}

#     outputDict['ID'] = cursorObj[0]
#     outputDict['NI_ID'] = cursorObj[1]
#     outputDict['JOB_TITLE'] = cursorObj[2]

#     return outputDict

# if _name_ == "__main__":
#     sqlLine = readSQL()
#     connectionString = sqlConnect()

#     sanjOp = {}

#     for rowLine in sqlLine:
#         execResult = executeSQLQuery(connectionString, rowLine)
#         for rows in execResult:
#             print(rows)

#     # outputResult = list(sqlConnect())
#     finalListOutput = [getCursorData(row) for row in outputResult]
#     outputJson = {}
#     outputJson['Result'] = finalListOutput
    
    # """ Below code is used to create a json file if not available and dumps the output """
    # with open('data.json', 'w') as file:
    #     json.dump(outputJson, file)

    # """ below code with append the out to already available json file """
    # with open('data.json', 'w') as file:
    #     json.zzzzzzzz(outputJson, file)


    # Ram's expectation is to have two lines of json object in a data.json file.
    # Here's tee sample, 

    # {'result1': [{},{},{}]}
    # {'result2': [{},{},{}]}


import json
intellipaat = {"course":"python", "topic":"Python JSON"}
intellipaat_json = json.dumps(intellipaat)

print(type(intellipaat_json))

testFile = open('test.json', 'w')

for i in range(1,5):
    testFile.write(intellipaat_json + "\n")


test = {}
for i in range(0,10):
    test['result'+str(i)] = []

print(test)