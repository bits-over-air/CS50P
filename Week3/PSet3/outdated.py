month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date =input("Date:")
    date = date.strip().title()
    #Format 1
    if "/" in date:
        try:
            m,d,y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            if 1<= m <=12 and 1 <=d <=31:
                print(f"{y:04d}-{m:02d}-{d:02d}")
                break
        except:
            pass

#Format 2
    elif "," in date:
        try:
            month_name ,day_comma,year =date.split()
            day = int(day_comma .replace(",",""))
            year =int(year)
            month_name = month_name.title()

            if month_name in month and 1<=day<=31:
                m = month.index(month_name)+1
                print(f"{year:04d}-{m:02d}-{day:02d}")
                break
        except:
            pass



