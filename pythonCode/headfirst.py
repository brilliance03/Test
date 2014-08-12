#!/usr/bin/env python
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
		  ["Graham Chapman", ["Michael Palin", "John Cleese",
				      "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

#
for each_item in movies:
    print(each_item)

#
for each_item in movies:
    if isinstance(each_item,list):
	    for item_in_list in each_item:
		    print(item_in_list)
    else:
            print(each_item)


#
for each_item in movies:
    if isinstance(each_item,list):
	    for item_in_list in each_item:
		    if isinstance(item_in_list,list):
			    for deepitem in item_in_list:
				    print(deepitem)
		    else:
			    print(item_in_list)
    else:
	    print(each_item)

