import pickle

class AthleteList(list):
    def __init__(self, a_name, a_dob = None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return(sorted(set(sanitize(t) for t in self))[0:3])


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins,secs) = time_string.split(splitter)

    return(mins + '.' + secs)


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            dataList = data.strip().split(',')

            return(AthleteList(dataList.pop(0),
                               dataList.pop(0),
                               dataList))
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return(None)

            

def put_to_store(file_list):
        all_athletes = {}

        for a_file in file_list:
            tmpData = get_coach_data(a_file)
            all_athletes[tmpData.name] = tmpData

        try:
            with open('athlete.pickle','wb') as athf:
                pickle.dump(all_athletes,athf)
        except IOError as ioerr:
            print('File error (put_and_store): ' + str(ioerr))
            
        return(all_athletes)

def get_from_store():
    all_athletes = {}

    try:
        with open('athlete.pickle','rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_from_store): ' + str(ioerr))

    return(all_athletes)


