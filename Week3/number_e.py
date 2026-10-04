#ValueError:
try:
    x =  int(input("What's x ?"))
    print (f"x is {x}")
except ValueError:
    print("x is not an integer")

#NameError:Adding else to existin try/except
try:
    y =  int(input("What's y ?"))
except ValueError:
    print("y is not an integer")
else:
    print (f"y is {y}")

#Using loops and giving user multiple chances 
#break can be after line 20 too without the else 
while True:
    try:
        z =  int(input("What's z ?"))
    except ValueError:
        print("z is not an integer")
    else:
        break

print(f"z is {z}")

#defining function for the same as z . Ca get rid of the esle block on 
#and return .use return while asking for input . else block is also correct
#but line 38 makes it more compact 
#Using Pass instead of asking to user try again and again.
#After except block instead os print statement ,pass 
#using prompt 
def main():
    #a = get_int() 
    a = get_int("What's a ?")
    print(f"a is {a}")

def get_int(prompt):
    while True:
        try:
            #return int(input("What's a ?"))
            return int(input(prompt))
        except ValueError:
            pass
            #print("a is not an integer")
        #else:
             #return a 


main()

