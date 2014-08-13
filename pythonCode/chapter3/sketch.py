data = open("sketch.txt")

separator = ":"

data.seek(0)

for each_line in data:
    if each_line.find(separator) >= 0:
        (role, line_spoken) = each_line.split(separator,1)
        print(role, end="")
        print(" said", end="")
        print(line_spoken, end="")
    else:
        continue

data.close()
