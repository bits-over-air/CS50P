def main():
    time_str = input("What time is it?")
    time_str = time_str.strip().lower()

    time = convert(time_str)

    if 7 <= time <= 8:
        print("breakfast time")
    elif 12<= time <=13:
        print("lunch time")
    elif 18<= time <=19:
        print("dinner time")
    #if not meal time , print nothing

def convert(time):
    #challenge:removing am/pm part first
    is_pm = False
    is_am = True

    if "p.m" in time or "pm" in time:
        is_pm = True
        time = time.replace("a.m.","").replace("p.m.","").replace("am","").replace("pm","").strip()
        is_am = True
        time = time.replace("a.m.","").replace("p.m.","").replace("am","").replace("pm","").strip()


    hours,minutes =time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    #challenge:converting 12-hour to 24-hour
    if is_pm and hours !=12:
        hours += 12
    if is_am and hours == 12:
        hours = 0

    return hours + minutes /60

if __name__ == "__main__":
    main()



