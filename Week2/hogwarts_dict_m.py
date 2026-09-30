#list of dictionaries 
students = [ 
    {"name": "Hermione","house":"Gryffindor","patronus":"Otter"},
    {"name": "Draco","house":"Slytherin","patronus":"None"},
    {"name": "Harry","house":"Gryffindor","patronus":"Stag"},
    {"name": "Ron","house":"Gryffindor","patronus":"Jack Russel terrier"}
]

for student in students:
    print(student["name"], student ["house"], student["patronus"], sep = ",")