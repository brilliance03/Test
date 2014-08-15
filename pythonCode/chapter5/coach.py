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
        return(data.strip().split(','))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)
    

def format_datalist(datalist,number=3):
    try:
        clean_list = []
        for item in datalist:
            clean_list.append(sanitize(item))
        unique_list = set(clean_list)
        return(sorted(unique_list)[0:number])
    except TypeError as tyerr:
        print('Data error: ' + str(tyerr))


sarah = get_coach_Data('sarah2.txt')
(sarah_name,sarah_dob) = sarah.pop(0),sarah.pop(0)
print(sarah_name + "'s fastest time are: " + str(format_datalist(sarah)))

