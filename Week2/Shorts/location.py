#getting co-ordinate by combining latitude and longitude
# using tuple . cannot add or change a value inside tuples.
import sys
def main():
    coordinates =(42.376 , -71.115)
    #unpacking in lat and long
    latitude, longitude = coordinates
    print(f"Latitude: {coordinates[0]}") #returning the 
    #latitude part of value .
    print(f"Longitude: {coordinates[1]}")

    
#getting size of tuple and list 
    coordinate_tuple = (42.376 ,-71.115)
    coordinate_list = [42.376 ,-71.115]
    print(f"{sys.getsizeof(coordinate_tuple)} bytes")
    print(f"{sys.getsizeof(coordinate_list)} bytes")

main()