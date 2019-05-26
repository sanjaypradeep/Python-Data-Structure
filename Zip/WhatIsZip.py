# zip() in Python
# The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

# Python code to demonstrate the working of
# zip()


# Here's the example..


name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

print (mapped) # output: <zip object at 0x10191e208>

# to get values from zip object, converting zip object into set
mapped = set(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped) # The zipped result is : {('Manjeet', 4, 40), ('Shambhavi', 3, 60), ('Nikhil', 1, 50), ('Astha', 2, 70)}


#Here's is one other example, 
subject = ['English', 'Hindi', 'Tamil', 'Math']
teachernames = ['Ram', 'Lalitha', 'Gowri']


# if you see the above two list, there are 3 teachers available inside a list, and there are four subjects

# Here we are trying to map each teacher on each subject, so lets zip it. 

result = zip(subject, teachernames)
print ("The zipped result is .. ", dict(result))

# output will be - {'English': 'Ram', 'Hindi': 'Lalitha', 'Tamil': 'Gowri'}

# Explanation : from the above result, you can understand there's no teacher is been assinged for subject Map, that's because there're only 3 teachers available right now. 
# length mismatches.


# Hey I have a question now?

# I need a dictionary as output saying, the subject which is not having teacher as well. something like.. {'English': 'Ram', 'Hindi': 'Lalitha', 'Tamil': 'Gowri', 'Math': None}


# here's the solution, 
finalOp = {}

def needOutput(sub, professors):
	if len(sub) > len(professors):
		finalOp = dict(zip(sub, professors))
		finalOp = includedMissedEleement(finalOp, sub)
		return finalOp
	elif len(professors) > len(sub):
		finalOp = dict(zip(professors, sub))
		finalOp = includedMissedEleement(finalOp, professors)
		return finalOp
	else:
		return dict(zip(sub, professors))


def includedMissedEleement(op, listToCheck):
	for i in listToCheck:
		if i not in op:
			op[i] = None
	return op

desiredOutput = needOutput(subject, teachernames)
print(desiredOutput)

# the above output is desired only in case of more subjects than teachers.

# what if there're more teachers than subjects.

subject = ['Tamil', 'English']
teacherNames = ['Ram', 'Tamanna', 'Lita']

finaOutput = needOutput(subject, teacherNames)
print(finaOutput)