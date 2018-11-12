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