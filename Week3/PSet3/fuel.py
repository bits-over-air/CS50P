while True:
    try:
        s =input("Fraction:")
        x,y = s.split("/")
        x = int(x)
        y = int(y)
        if y == 0 :
            raise ZeroDivisionError
        if x > y or x < 0 or y < 0 or x > y:
            raise ValueError
        break
    except(ValueError,ZeroDivisionError):
        pass

p = round(x / y * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")
