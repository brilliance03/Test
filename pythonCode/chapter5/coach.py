class Athlete:
    def __init__(self, a_name, a_dob = None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set(sanitize(t) for t in self.times))[0:3])

    def add_time(self,time):
        self.times.append(time)

    def add_times(self,times):
        self.times.extend(times)

    

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
            '''
            dataDict = {'name':dataList.pop(0),
                        'dob':dataList.pop(0),
                        'times':dataList,
                        'best3':sorted(set(sanitize(t) for t in dataList))[0:3]}
            return(dataDict)'''
            return(Athlete(dataList.pop(0),
                           dataList.pop(0),
                           dataList))
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
##print(sarah['name'] + "'s fastest time are: " + str(sarah['best3']))
print(sarah.name + "'s fastest time are: " + str(sarah.top3()))
sarah.add_times(['1.11','3:12','4-15'])
sarah.add_time('1.00')
print(sarah.name + "'s fastest time are: " + str(sarah.top3()))
