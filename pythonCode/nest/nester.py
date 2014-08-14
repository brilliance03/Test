'''this is the "nester.py" module and it provides one function
    called print_lol() which prints lists that may or may not
    include nested lists.'''

'''edition 2 add another param called level'''
'''edition 3 add another param called indentation'''
'''edition 4 add another param called ouput'''
import sys

def print_lol(the_list, indentation=False, level=0, output=sys.stdout):
    '''this function takes one positional argument called "the_list", which
        is amy Python list (of - possibly - nested lists). Each data item in
        the provided list is (recursively) printed to the screen on it's own
        line'''
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indentation,level+1,output)
        else:
            if indentation:
                for num in range(level):
                    print("\t", end="",file=output)
            print(each_item,file=output)
            
