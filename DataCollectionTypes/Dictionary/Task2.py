org = []
def getOrgNames(fromGivenInput):
    for orgInfo in fromGivenInput:
        if not orgInfo['orgName'] in org:
            org.append(orgInfo['orgName'])
    return org

def employeeInfoBasedOnOrg(orgName, userGivenInput):
    output = { orgName : []}
    tempOp = {}

    for info in userGivenInput:
        if info['orgName'] == orgName:
            tempOp[info['empName']] = info['empSal']
            
    output[orgName].append(tempOp)
    print(output)

if __name__ == '__main__':

    givenInput = [ 
                    {
                    "orgName": "techM",
                    "empName": "name1",
                    "empSal": "40000"
                    },
                    {
                    "orgName": "techM",
                    "empName":"name2",
                    "empSal": "5000"
                    },
                    {
                    "orgName": "techM",
                    "empName": "name3",
                    "empSal": "50000"
                    },
                    {
                    "orgName": "Mahindra",
                    "empName": "name4",
                    "empSal": "55000"
                    },
                    {
                    "orgName": "Mahindra",
                    "empName": "name5",
                    "empSal": "45000"
                    },
                    {
                    "orgName": "Mahindra",
                    "empName": "name6",
                    "empSal": "35000"
                    }
                ]


    listOfOrgs = getOrgNames(givenInput)

    for orgName in listOfOrgs:
        employeeInfoBasedOnOrg(orgName, givenInput)


from collections import Counter

eop = {}
d1 = {'apple': 'sanjay', 'orange': 'sanjay', 'banana': 'sanjay'}

# for k,v in d1.items():
#     if type(v) == str:
#         eop[k] = len(v)

# print(Counter(eop))

print(Counter({k:len(v) for k,v in d1.items()}))