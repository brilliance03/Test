#!/usr/bin/env python
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91,
		  ["Graham Chapman", ["Michael Palin", "John Cleese",
				      "Terry Gilliam", "Eric Idle", "Terry Jones"]]]

'''define a function to handle the list'''
def print_lol(the_list):
    for item_in_list in the_list:
        if isinstance(item_in_list,list):
            print_lol(item_in_list)
        else:
            print(item_in_list)

'''define a function to print separator'''
def print_separator():
    print "=" * 60

'''handle the one dimension list'''
for each_item in movies:
    print(each_item)

print_separator()

'''handle the two dimension list'''
for each_item in movies:
    if isinstance(each_item,list):
	    for item_in_list in each_item:
		    print(item_in_list)
    else:
            print(each_item)
            
print_separator()

'''handle the three dimension list'''
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
	    
print_separator()

print_lol(movies)

print_separator()

