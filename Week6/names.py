"""names =[]

for _ in range(3):
    name = input("What is your name ?")
    names.append(name)


for name in sorted(names):
    print(f"hello , {name}")"""

#open =opens a new file names.txt will get created and w 
# will write and store the names
#open with = opens and closes a file . so accidentally 
#if you forget to add file.close()

"""name = input("What's your name? ")

file = open("names.txt","a") # w will rewrite the names,not append, a will append

file.write(f"{name} \n")# will write the name to file .
#To avoid no spaces writing as a f string and adding a new line
file.close()# Will close the file"""

#Alternate way of writing the above :
name = input("What's your name? ")

with open("names.txt","a") as file:
    file.write(f"{name}\n")

    