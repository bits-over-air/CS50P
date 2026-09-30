#Using lists in for 
for i in range (3):
    print("meow")

for j in [0,1,2]:
    print("woof")

print ("moo \n" * 3, end = "") #n for newline, end so as not to  get a new blank line

#while and break:
while True :
    n = int (input("What's n?"))
    if n > 0:
        break 

for _ in range(n):
    print("meoww")