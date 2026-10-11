import random 


number = random.randint(1,10)
print(number)

# using random.shuffle
cards = ["jack","queen","king"]
random.shuffle(cards)
for card in cards:
    print(card)
