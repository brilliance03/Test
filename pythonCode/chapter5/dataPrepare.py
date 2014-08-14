with open('james.txt','r') as james_data:
    data = james_data.readline()
james = data.strip().split(',')

with open('julie.txt') as julie_data:
    data = julie_data.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mikey_data:
    data = mikey_data.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as sarah_data:
    data = sarah_data.readline()
sarah = data.strip().split(',')

print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))


print("=" * 70)

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return (time_string)

    (minut,second) = time_string.split(splitter)
    return (minut + "." + second)


##clean_james = []
##clean_julie = []
##clean_mikey = []
##clean_sarah = []
##
##for each_item in james:
##    clean_james.append(sanitize(each_item))
##
##for each_item in julie:
##    clean_julie.append(sanitize(each_item))
##
##for each_item in mikey:
##    clean_mikey.append(sanitize(each_item))
##
##for each_item in sarah:
##    clean_sarah.append(sanitize(each_item))
##
##
##print(sorted(clean_james))
##print(sorted(clean_julie))
##print(sorted(clean_mikey))
##print(sorted(clean_sarah))

print(sorted([sanitize(each_item) for each_item in james]))
print(sorted([sanitize(each_item) for each_item in julie]))
print(sorted([sanitize(each_item) for each_item in mikey]))
print(sorted([sanitize(each_item) for each_item in sarah]))

unique_james = []

##for each_item in sorted([sanitize(each_item) for each_item in james]):
##    if each_item not in unique_james:
##        unique_james.append(each_item)

##print(unique_james[0:3])

print(sorted(set([sanitize(each_item) for each_item in james]))[0:3])



