x = int (input ("Enter a number x:"))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Define main 
def main():
    y = int(input("Enter a number y:"))
    if is_even(y):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    """"if n % 2 ==0: this is correct too 
        return True
    else:
        return False """
    return n % 2 == 0

main()
