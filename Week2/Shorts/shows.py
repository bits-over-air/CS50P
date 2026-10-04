#apporpriate capitalization , spaces 
SHOWS = [
    "avatar : The last airbender",
    "ben 10",
    "Arthur",
    " Spongebob Squarepants",
    "Phineas and Ferb",
    "Kim Possible",
    "Jimmy Neutron",
    "The Proud Family"
]

def main():
    cleaned_shows = []
    #for show in SHOWS:
        #print(show.strip().title())
    for show in SHOWS:
        cleaned_shows.append(show.strip().title())

    print (', '.join(cleaned_shows))


main()