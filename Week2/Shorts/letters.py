def main():
#List for guest names , can use the list name instead of i 
    names =["Mario", "Luigi", "Daisy","Yoshi","Bowser"]
    for name in names:
        #print(names[i])-Prints the names in the list 
        print(write_letter(name,"Princess Peach"))

    #print(write_letter("Mario","Princess Peach"))
    #print(write_letter("Luigi","Princess Peach"))
    #print(write_letter("Daisy","Princess Peach"))
    #print(write_letter("Yoshi","Princess Peach"))

# Using Python f-strings here to interpolate values of 
# rx and sender .
def write_letter(receiver,sender):
    return f"""
    ===================================

        Dear {receiver},

        You are cordially invited to a ball at 
        Peach's castle this evening , 7.00 PM

        Sincerely ,
        {sender}
    =====================================
    """

main()