#Reading an existing file
#open = opens an existing file , readlines just reads the lines
#for loop for reading the lines and printing thm out
with open ("names.txt" , "r") as file : # reads the lines 
    lines = file.readlines()

for line in lines:
    print("hello,", line)#rstrip =stripping out whitspace/new lines


#Alternate way of writing for above
with open("names.txt","r") as file:
    for line in file:
        print("hello,",line.rstrip())

#Sorting hellos reversing the names
names =[]

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names,reverse =True):
    print(f"hello,{name}")

#Alternate way to write sorted hellos
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,",line.rstrip())