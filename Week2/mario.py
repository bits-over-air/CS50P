"""for _ in range(3):
    print("#")"""

def main():
    print_column(3)


"""def print_column(height):
    for _ in range(height):
        print("#")"""
# Reusing print column in different ways 
def print_column(height):
    print("#\n" * height, end ="")

#main does not need to know the underlying implementation of print function has changed

main()