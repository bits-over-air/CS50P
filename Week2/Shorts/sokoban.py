#Goal of this program is to take as input an action the user  might 
#take in the game -move up , down , right or left and storing that 
#action inside a history of actions 

def main ():
    history =[]

    while True:
        action = input("Action:")
        if action == "Undo":
            undone = history.pop() #Removing the elementfrom list
            print(f"Undone:{undone}")
        elif action == "Restart":
            history.clear()
        else:
            history .append(action)
        
        print(history)


main()