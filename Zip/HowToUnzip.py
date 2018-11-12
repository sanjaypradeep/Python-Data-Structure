# How to unzip?
# Unzipping means converting the zipped values back to the individual self as they were. This is done with the help of “*” operator

# Python code to demonstrate the working of
# unzip

# initializing lists

name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", mapped)


# =====================================Unzipping===============================================

# it's not but getting the values from object,

namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", namz)

print("The roll_no list is : ", roll_noz)

print("The marks list is : ",marksz)

# Practical Applications: There aremany possible applications that can be said to be exected using zip,
# be it student database or scorecard or any other utility that requires mapping of groups.A small example of scorecard is
# demonstrated below.

# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player :  %s     Score : %d" % (pl, sc))