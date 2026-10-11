#pip install cowsay 
import cowsay 
import sys 

if len(sys.argv) == 2 :
    cowsay.cow("hello, " + sys.argv[1]) # can do trex too instead of cow