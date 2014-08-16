def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins,secs) = time_string.split(splitter)

    return(mins + '.' + secs)


def get_coach_Data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
        #return(data.strip().split(','))
            dataList = data.strip().split(',')
            dataDict = {'name':dataList.pop(0),
                        'dob':dataList.pop(0),
                        'times':dataList,
                        'best3':sorted(set(sanitize(t) for t in dataList))[0:3]}
            return(dataDict)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)
    

def format_datalist(datalist):
    try:
        clean_list = []
        for item in datalist:
            clean_list.append(sanitize(item))
        unique_list = set(clean_list)
        return(sorted(unique_list))
    except TypeError as tyerr:
        print('Data error: ' + str(tyerr))


sarah = get_coach_Data('sarah2.txt')
#(sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
##sarahDict = {'name':sarah.pop(0),'dob':sarah.pop(0),'times':sarah}
print(sarah['name'] + "'s fastest time are: " + str(sarah['best3']))

