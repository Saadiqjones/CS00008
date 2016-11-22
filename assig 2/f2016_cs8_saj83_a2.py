import os
total_distance = 0
total_lines = 0
file = "something"

def processFile(file):
    distance = 0
    if os.path.isfile(file):
        input_file = open(file, 'r')
        lines = 0
        for line in input_file:
            info = line.split(',')
            distance += float(info[1])
            lines += 1
        input_file.close()
        
        total_distance += distance
        total_lines += lines
        print('Partial Total # of lines:', lines)
        print('Partial distance run:', distance)
    else:
        print('No file found')

        
def printKv(key,value,klen = 0):
    if klen > 0:
        print(key.substr(0,klen) + ':', value)
    else:
        print(key + ':', value)

while 1 == 1:
    file = input("File to be read: ")
    if file == "" or file == "q" or file == "quit":
        break
    else:
        processFile(file)

print('Totals')
print('Total # of lines:', total_lines)
print('Total distance run:', total_distance)
        



        

