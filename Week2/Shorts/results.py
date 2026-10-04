#making a list in python for results
results=["Mario","Luigi",]

results.append("Princess") #Append adds new elemts to the existing list
results.append("Yoshi")
results.append("Koopa Troopa")
results.append("Toad")
#Appending a list to the existing list
results.append(["Bowser","Donkey Kong Jr."])
#removing the above from the list
results.remove(["Bowser","Donkey Kong Jr."])
#extend adds new list to th existing list
results.extend(["Bowser","Donkey Kong Jr."])
results.remove("Bowser")
#insert takes as its first arg the index at which I want to
#insert some given element .
results.insert(0,"Bowser")
results.reverse()# reverses the list 

print(results)