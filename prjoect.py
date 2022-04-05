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
                
