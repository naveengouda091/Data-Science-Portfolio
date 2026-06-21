
'''
sys module provides access to some variables used or maintained 
by the interpreter and to functions that interact strongly with 
the interpreter.
sys.argv is a list in Python, 
which contains the command-line arguments passed to the script.
The first element of the list, sys.argv[0], is the name of the 
script itself.
The second element, sys.argv[1], is the first argument passed 
to the script,
and so on.
'''

import sys 

'''
try:
    print("hello", sys.argv[1])
except IndexError:
    print("too few args")
    
    
'''

if len(sys.argv)<2:
    sys.exit("too few arguments")
#elif len(sys.argv)>2:
    #sys.exit("too many arguments")
#else :
    #print("hello, ", sys.argv[1])

for arg in sys.argv[1:]:
    print("hello, ",arg)

#packages 



