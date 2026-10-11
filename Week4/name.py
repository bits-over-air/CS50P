import sys

#print("hello my name is ", sys.argv[1])
# hnadling index error if user does not know they need to type
#their name as python3 name.py Vandana put a try block
"""try:
    print("hello my name is ", sys.argv[1])
except IndexError:
    print("Too few arguments")"""

# Another way to handle without the try block 
# whole name or more than 2 then put name in ""
#python3 name.py "Vandana Shah"

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")#print the message and exit
else:
    print("hello my name is ", sys.argv[1])

