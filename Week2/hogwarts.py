students =["Hermione","Harry","Ron"]

#can normally print yhe students with list student[0]student[1]in seaparate lines 
#but if the list is longer and ont know thepositions ,use for loop
"""for student in students:
    print(student)"""
#Do not need to initialize variable earlier . can initialize directly in loop 

for i in range (len(students)):
    print(i+1,students[i])