# Supports multiple words in sysargv

import sys 

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]: # slicing index0 since its name of program
    print("hello ,my name is",arg)