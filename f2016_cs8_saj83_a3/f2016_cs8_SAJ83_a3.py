#
# MN: the header with user, instructor and course info
#
# Notes
# MN: why do you define function within function?
# MN: you need to experiment a little bit more with code
# MN: I suggest to read the assignment more carefully
# MN: it is good to reuse code, but here you re-used a little bit to much the code from assignment #2
#

# MN: what does this function do? and why do you defined it in here within the other function?
# MN: you do not need to pass in the file handle, that you do not use
#     we need to pass in the list of data
def sum_list(data_list):
    sum_numbers = 0
    # MN: you need to loop on the all data list passed in input
    #for x in items:
    for item in data_list:
        # MN: item is a list of 2 values: name and distance
        #sum_numbers += x
        sum_numbers += item[1]
    return sum_numbers


# MN: what does this function do? and why do you define it here
# MN: you need to pass in th elist of data, not the file handle
#def smallest_num_in_list( fh ):
def smallest_num_in_list( data_list ):
    # MN: where is this list defined?
    #min = list[ 0 ]
    min = data_list[0][1]
    # MN: use input argument
    #for a in list:
    for a in data_list:
        if a[1] < min:
            min = a[1]
    return min


# MN: what does this function do? and why do you define it here
# MN: please check the comments in the previous function
#def max_num_in_list( fh ):
def max_num_in_list( data_list ):
    #max = list[ 0 ]
    max = data_list[0][1]
    #for a in list:
    for a in data_list:
        if a[1] > max:
            max = a[1]
    return max

def processFile(fh):
    # count how many lines the files has and sum the distance that is the second field of each line
    #
    # initialize partial accumulators
    # partial total distance
    ptd = 0
    # partial total number of lines
    ptn = 0

    # MN: what does this function do? and why do you defined it in here within the other function?
    # MN: moved before this function
    #def sum_list(fh):
    #    sum_numbers = 0
    #    for x in items:
    #        sum_numbers += x
    #    return sum_numbers
    # MN: why do you call this function here?
    #     you are missing the input argument, you defined this function to accept in input a file handle
    #     but you call it without
    #print(sum_list())

    # MN: what does this function do? and why do you define it here
    # MN: moved before this function
    #def smallest_num_in_list( fh ):
    #    min = list[ 0 ]
    #    for a in list:
    #        if a < min:
    #            min = a
    #    return min
    # MN: again you are calling a function that is expecting an input argument but you do not provide it
    #print('Min distance run by participant:', smallest_num_in_list)

    # MN: what does this function do? and why do you define it here
    # MN: moved before this function
    #def max_num_in_list( fh ):
    #    max = list[ 0 ]
    #    for a in list:
    #        if a > max:
    #            max = a
    #    return max
    # MN: again you are calling a function that is expecting an input argument but you do not provide it
    #print('Max distance run by participant:', max_num_in_list)

    # MN: you need to define a list where to store the data read
    data = []
    # loops on all the lines in the files
    # we hope that the read position is at the beginning of the file
    for line in fh:
        # in each iteration, we got the next line from the file
        #
        # MN: we need to make sure that we discard the headers
        if 'distance' in line:
            continue

        # remove new line (/n) and split in two parts: name and number
        [name, distance] = line.rstrip('\n').split(',')
        # convert distance from string to float
        distance = float(distance)
        # print name and distance in this record properly formatted
        # MN: why do you print all the values that you are reading.
        #     there are why too many to be useful to see them on the screen
        #printKV('Name', name, FORMAT_KEY_LENGTH)
        #printKV('Distance', distance, FORMAT_KEY_LENGTH)
        #
        # MN: we do not need this accomulators
        # update partial accumulators
        # partial total distance
        #ptd += distance
        # partial total number of lines
        #ptn += 1
        #
        # MN: insert new values in list
        data.append([name, distance])
    # for
    #
    # MN: you need to return all the values read
    # returns partials
    #return [ptn, ptd]
    return data

# MN: here you are done with defining the function processFile
#     Now you need to write the main body of the program
#     You need to adjust the indentation

#    # initialize totals partials
#    # total distance
#    td = 0
#    # total number of lines
#    tn = 0
#    # number of files
#    nf = 0

#    #
#    #  ask the user for the first file
#    print('Please enter the name of the first file to process.')
#    file = input('File name : ')

#    # check if file name is empty, or is q or quit and also if
#    while ( file != '' and file != 'quit' and file != 'q' and os.path.exists(file) ):

#        # open the file in read mode and creates the file object
#        fh = open(file, 'a+')
#        # process the file and get the number of lines and the sum of the distances
#        ptn, ptd = processFile(fh)
#        # close the file
#        fh.close()

#        # print partials properly formatted with spacing before and after
#        print('')
#        printKV('Partial Names found', ptn, FORMAT_KEY_LENGTH)
#        printKV('Partial Distance', ptd, FORMAT_KEY_LENGTH)
#        print('')

#        # update total accumulators
#        # number of files
#        nf += 1
#        # total distance
#        td += ptd
#        # total number of lines
#        tn += ptn

#        # ask the user the next file
#        print('Please enter the name of the next file to process. Leave empty or type q/quit to exit')
#        file = input('File name : ')

#    #while

#    # print report
#    print('')
# MN: function printKV is not defined.
#     how can you use something that is not defined?
#    printKV('Number of input Files read', nf, FORMAT_KEY_LENGTH)
#    printKV('Total Distance run', td, FORMAT_KEY_LENGTH)
#    printKV('Total number of participants:', tn, FORMAT_KEY_LENGTH)
#    print('')
    
# initialize totals partials
# total distance
td = 0
# total number of lines
tn = 0
# number of files
nf = 0

#
#  ask the user for the first file
# MN: you need to ask only for the mast list file
#     the content of the file will tell you which are the data files
print('Please enter the name of the first file to process.')
file = input('File name : ')

# MN: open the master list file and read the data files
data_files = []
fh = open(file,'r')
for line in fh:
    data_files.append(line.strip('\n'))
fh.close()

# MN: you need to collect all the data in one big long list
data = []
# check if file name is empty, or is q or quit and also if
# MN: you do not need to use a while loop, but a for loop
# while ( file != '' and file != 'quit' and file != 'q' and os.path.exists(file) ):
for file in data_files:

    # open the file in read mode and creates the file object
    # MN: you are just reading the data file, so open the file for reading
    #fh = open(file, 'a+')
    fh = open(file,'r')
    # process the file and get the number of lines and the sum of the distances
    # MN: according to my fixes, you get back only the list of all the lines read
    #ptn, ptd = processFile(fh)
    file_data = processFile(fh)
    # close the file
    fh.close()

    # MN: now you combine the data read from this file with the master list
    data += file_data
# end for

#        # update total accumulators
#        # number of files
#        nf += 1
#        # total distance
#        td += ptd
#        # total number of lines
#        tn += ptn

#        # ask the user the next file
#        print('Please enter the name of the next file to process. Leave empty or type q/quit to exit')
#        file = input('File name : ')

#    #while

# MN: number of files read
nf = len(data_files)
# MN: total distance run
td = sum_list(data)
# MN: number of participants
# MN: extract all the names without duplicates
name_list = []
# MN: loop on all the data
for item in data:
    # MN: name is the first element of item
    # MN: check if name is already in list
    if item[0] not in name_list:
        # MN: new name. insert it in list
        name_list.append(item[0])
# MN: now you can find total number of participants
tn = len(name_list)

# print report
print('')
print('Number of input Files read : ', str(nf))
print('Total Distance run ........: ', str(td))
print('Total number of participants:', str(tn))
print('')
