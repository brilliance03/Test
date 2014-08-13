'''this is the "nester.py" module and it provides one function
    called print_lol() which prints lists that may or may not
    include nested lists.'''

'''edition 2 add another param called level'''

def print_lol(the_list, indentation=False, level=0):
    '''this function takes one positional argument called "the_list", which
        is amy Python list (of - possibly - nested lists). Each data item in
        the provided list is (recursively) printed to the screen on it's own
        line'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indentation,level+1)
        else:
            if indentation:
                for num in range(level):
                    print("\t", end="")
            print(each_item)
            
