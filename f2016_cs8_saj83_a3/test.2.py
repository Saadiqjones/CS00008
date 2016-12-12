def processFile(fh):
    # count how many lines the files has and sum the distance that is the second field of each line
    #
    # initialize partial accumulators
    # partial total distance
    ptd = 0
    # partial total number of lines
    ptn = 0
    
    def sum_list(fh):  
        sum_numbers = 0  
        for x in items:  
            sum_numbers += x  
        return sum_numbers  
    print(sum_list())  

    def smallest_num_in_list( fh ):  
        min = list[ 0 ]  
        for a in list:  
            if a < min:  
                min = a  
        return min  
    print('Min distance run by participant:', smallest_num_in_list)  

        def max_num_in_list( fh ):  
        max = list[ 0 ]  
        for a in list:  
            if a > max:  
                max = a  
        return max  
    print('Max distance run by participant:', max_num_in_list) 
    # loops on all the lines in the files
    # we hope that the read position is at the beginning of the file
    for line in fh:
        # in each iteration, we got the next line from the file
        #
        # remove new line (/n) and split in two parts: name and number
        [name, distance] = line.rstrip('\n').split(',')
        # convert distance from string to float
        distance = float(distance)
        # print name and distance in this record properly formatted
        printKV('Name', name, FORMAT_KEY_LENGTH)
        printKV('Distance', distance, FORMAT_KEY_LENGTH)
        #
        # update partial accumulators
        # partial total distance
        ptd += distance
        # partial total number of lines
        ptn += 1
    # for
    #
    # returns partials
    return [ptn, ptd]
    
    # initialize totals partials
    # total distance
    td = 0
    # total number of lines
    tn = 0
    # number of files
    nf = 0

    #
    #  ask the user for the first file
    print('Please enter the name of the first file to process.')
    file = input('File name : ')

    # check if file name is empty, or is q or quit and also if
    while ( file != '' and file != 'quit' and file != 'q' and os.path.exists(file) ):

        # open the file in read mode and creates the file object
        fh = open(file, 'a+')
        # process the file and get the number of lines and the sum of the distances
        ptn, ptd = processFile(fh)
        # close the file
        fh.close()

        # print partials properly formatted with spacing before and after
        print('')
        printKV('Partial Names found', ptn, FORMAT_KEY_LENGTH)
        printKV('Partial Distance', ptd, FORMAT_KEY_LENGTH)
        print('')

        # update total accumulators
        # number of files
        nf += 1
        # total distance
        td += ptd
        # total number of lines
        tn += ptn

        # ask the user the next file
        print('Please enter the name of the next file to process. Leave empty or type q/quit to exit')
        file = input('File name : ')

    #while

    # print report
    print('')
    printKV('Number of input Files read', nf, FORMAT_KEY_LENGTH)
    printKV('Total Distance run', td, FORMAT_KEY_LENGTH)
    printKV('Total number of participants:', tn, FORMAT_KEY_LENGTH)
    print('')
    
