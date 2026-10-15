def main():
    while True:
        try:
            s = input("Fraction:")
            p = convert(s)
            break
        except(ValueError,ZeroDivisionError):
            pass
    print(gauge(p))

def convert(s):
    x,y = s.split("/")
    x = int(x)
    y = int(y)
    if y == 0 :
        raise ZeroDivisionError
    if x > y or x < 0 or y < 0 or x > y:
        raise ValueError
    return round(x / y * 100)

def gauge(p):
    if p <= 1:
        return "E"
    elif p >= 99:
        return "F"
    else:
        return f"{p}%"

if __name__ == "__main__":
    main()
