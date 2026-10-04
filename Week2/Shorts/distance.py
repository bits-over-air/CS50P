#Dictionary where names of spcaecrafts is one column and the 
#distances of the spacecraft is another column

distances = {
    "Voyager 1": 163,
    "Voyager 2" : 136,
    "Pioneer 10" : 80,
    "New Horizons" : 58,
    "Pioneer 11": 44
}

#Keys is another method in dictionaries that will return all keys.
def main():
    #for name in distances.keys():
        #print(f"{name} is {distances[name]} AU from Earth" )
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)} m")
#convert AU to meter
def convert(au):
    return au * 149597870700




main()