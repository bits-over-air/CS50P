text = input("Enter text:")
vowels ="aeiouAEIOU"
for c in text:
    if c not in vowels:
        print(c, end ="")

print()
