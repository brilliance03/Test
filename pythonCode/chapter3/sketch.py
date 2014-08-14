import nester
import pickle

try:
    data = open("sketch.txt")

    separator = ":"

    data.seek(0)

    man = []
    other = []

    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(separator,1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
            '''print(role, end="")
            print(" said", end="")
            print(line_spoken, end="")'''
        except ValueError:
            pass

    data.close()

except IOError:
    print("There has no such file.")


print(man)
print(other)
## code in normal
##try:
##    man_dataOut = open("man_data.txt","w")
##    other_dataOut = open("other_data.txt","w")
##
##    print(man,file=man_dataOut)
##    print(other,file=other_dataOut)
##
##except IOError:
##    print("Output ERROR")
##finally:
##    man_dataOut.close()
##    other_dataOut.close()

'''using <with> which can help you close file automatically'''
try:
    with open('man_data.txt','wb') as man_file, open('other_data.txt','wb') as other_file:
        #nester.print_lol(man,output=man_file)
        #nester.print_lol(other,output=other_file)
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('file error: ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error: ' + str(perr))
