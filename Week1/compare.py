x = int(input("Enter a value for x :"))
y = int(input("Enter a value for y :"))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
#elif x == y: can be written -not wrong but else is better
else:
    print("x is equal to y")

# using OR /== for the same comparison
a = int(input("Enter a value for a :"))
b = int(input("Enter a value for b :"))
#if a < b or a > b : can use equalto or not equal to also 
if a == b:
    print ("a is  equal to b ")
else:
    print("a is not equal to b")