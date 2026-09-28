"""#Ask user for their name"
name = input("What is your name ?").strip().title()
print("hello," ,name)

#ask user for their age"
age= input("What is your age ?")
print("Your age is " ,end="")
print(age)

#Ask user for their name"
name = input("What is your name ?")

#Removes whitespaces from name
#name = name.strip()

#Remove whitespaces from str and capitalize user's name 
name = name.strip().title()

#Capitalize user's name 
#name = name.capitalize()

#capitalize the first letter of each word
name = name.title()

print(f"hello, {name}")

#Split user's name into first and last 
name = input("What is your name ? ").strip().title()

first,last = name.split(" ")

#Say hello to user 
print(f"Hello,{first}")"""

def hello ():
    print("hello")

name = input("What is your name ?")
hello()
print(name)

#line 43 and 44 defining very own function hello
#defined to take parameter ,a single parameter as input
def hellos (to):
    print("hello",to)

names= input("What is your name ?")
#Not only calling hello,but passing name as input the name variables as an argument
#even though the variable is called names here when the fn itself is called
#the comp assumes the same value is now called To
hellos(names)

#defining a main fn -organizing the file and ordering the functions
def main():
    name = input("What is your name ?")
    heloos(name)

def heloos(to ="world"):
    print("hello,",to)


main()
