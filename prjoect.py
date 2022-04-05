ello = "ello"
# read csv file
import csv
                    
# organize data
def organize_data():
    fName = 'laposte_hexasmal.small.csv'
    with open(fName, newline='') as csvfile:
    fields = csv.reader(csvfile, delimiter=';')
    for field in fields:
        print(field[3], field[4], field[5])
     
    
    # haversine
from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r
