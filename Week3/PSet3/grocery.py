grocery = {}
while True:
    try:
        item =input()
        item= item.strip().upper()
        if item:
           grocery[item] = grocery.get(item ,0)+1
    except EOFError:
       print()
       break

for item in sorted(grocery):
    print(f"{grocery[item]} {item}")
