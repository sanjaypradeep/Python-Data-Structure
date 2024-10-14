# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     # what if query name value doesn't exist in student_marks?

#     if query_name in student_marks.keys():
#         studentScore = student_marks[query_name]
#         print(sum(studentScore)/ len(studentScore))
#     else:
#         print("student name not exist")


import textwrap

def wrap(string, max_width):
    emptyList= []
    for i in range(0,len(string),max_width): 
        emptyList.append(string[i:i+max_width])
    return "\n".join(emptyList)
  
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)