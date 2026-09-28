"""x = int(input("Enter a number x: "))
y = int(input("Enter a number y: "))


print(x+y)
#Divison
print(x/y)
#Number with decimals
a = float(input("Enter a number a:"))
b = float(input("Enter a number b: "))

print(a+b)

#Round-off decimals 
p = float(input("Enter a number p:"))
q = float(input("Enter a number q: "))

r = round( p+q )
s = round(p /q)
#Separating with commas 
print(f"{r:,}")
#Rounding off upto 2 decimal points 
print(f"{s:.2f}")"""

def main():
    x= int(input("What is x:"))
    print("x sqaured is ",sqaure(x))

def sqaure(n):
    #return n * n
    return pow(n,2)#pow(number ,exponent)

main()