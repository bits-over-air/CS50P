#Splitting the lines and using comma in row /column
with open("students.csv") as file:
    for line in file:
        #row =line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")
        name,house = line.rstrip().split(",")
        print(f"{name} is in {house}")

#Alternate way of writing the above:

#Sorting based on alphabets

students =[]

with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)


#Creating dict 
students =[]
with open("students.csv") as file:
    for line in file:
        name,house = line.rstrip().split(",")
        student ={"name":name ,"house":house}
        students.append(student)

def get_name(student):
    return student["name"]#can be house too


for student in sorted(students , key=get_name):#can use key =get_house
    print(f"{student['name']} is in {student['house']}")
