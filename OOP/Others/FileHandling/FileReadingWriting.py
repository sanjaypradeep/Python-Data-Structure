# Open a file
import time

with open('input1.txt', 'r+') as info:
    print ("Name of the file: ", info.name)
    print ("Closed or not : ", info.closed)
    print ("Opening mode : ", info.mode)
    # print ("Softspace flag : ", info.softspace)

    start= time.time()

    # line = info.readline()
    line2 = info.readlines()
    # line3 = info.xreadlines()
    # print ("line is ====",line)
    # print ("line 2 is ====",line2)
    # print ("line3 is ======", line3)
    for i,j in enumerate(line2):
        print (i, j)
        # if i == 4:
        #     print "Hey"
        #     print (j[0])
        #     j = info.write("Something I'm writing here!")
        #     print (j[5])

    # with open('file', 'r') as input_file, open('new_file', 'r+') as output_file:
    #     for line in input_file:
    #         if line.strip() == 'to replace':
    #             output_file.write('new line\n')
    #         else:
    #             output_file.write(line)

    # print ("time taken to read", (end-start))
    # print (data + "Hi")
    info.close()


# for line in fileinput.input('input1.txt', inplace=True):
#       print (line.rstrip().replace('Something Im writing here!', 'changed text'),)

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    print ("Lines ... ==== ")
    lines[line_num] = text
    print(lines)
    out = open(file_name, 'w')
    out.writelines(lines)
    out.close()

def afterReplacingDisplay(fileName):
    print('After replacin my text..here we go....')
    lines = open(fileName, 'r+').readlines()
    print(lines)

# replace_line('input1.txt', 0, 'hey this is goods\n')
# afterReplacingDisplay('input1.txt')

end = time.time()
print ("time difference: ", end - start)