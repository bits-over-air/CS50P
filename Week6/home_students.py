#Using csv reader
import csv 

students =[]

"""with open("home_students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader: 
        students.append({"name":name, "home": home})

for student in sorted(students , key=lambda student: student["name"]):#can use key =get_house
    print(f"{student['name']} is from {student['home']}")"""

#Using csv dictReader

with open("home_students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader: 
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students , key=lambda student: student["name"]):#can use key =get_house
    print(f"{student['name']} is from {student['home']}")
