'''
:USAGES:
        from tcase.tcase import input, create_input
        create_input()
        
        x = list(map(int, get_input())) # as usual
'''

import fileinput

global_input = []

def create_input():
    global global_input
    global_input = []
    for line in fileinput.input(files ='tcase/testcases'):
        global_input.append(line.replace('\n', ''))

# YES we are overriding input function.
def input(print_global_input = 0):
    global global_input
    if len(global_input)==0:
        raise Exception('No Test Case Found, Create Input by command - create_input()')
    if print_global_input:
        return global_input
    ret_data = global_input.pop(0)
    return ret_data