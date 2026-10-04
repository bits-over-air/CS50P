def main ():
    spacecraft = {"name": "James Webb Space Telescope"}
    #Adding new keys to the dictionary
    spacecraft.update({"distance":"0.01","orbit":"Sun"})
    print(create_report(spacecraft))

def create_report(spacecraft):
    return f"""
    ====================

    Name:{spacecraft.get("name","Unknown")}
    Distance :{spacecraft.get("distance","Unknown")} AU
    Orbit :{spacecraft.get("orbit","Unknown")}
    ======================
    """
main()
#When you dony have the value for the corresponding key
#Distance :{spacecraft.get("distance","Unknown")} AU