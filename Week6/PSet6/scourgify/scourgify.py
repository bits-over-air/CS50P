import sys
import csv

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
students = []
try:
    with open (sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                last,first = row["name"].split(",")
                first = first.strip()
                last = last.strip()
                students.append({"first":first,"last":last,"house":row["house"]})

    with open (sys.argv[2], "w" , newline ="") as csvfile:
            fieldnames = ['first','last','house']
            writer = csv.DictWriter(csvfile ,fieldnames=fieldnames)
            writer.writeheader()
            for student in students:
                 writer.writerow(student)

except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
