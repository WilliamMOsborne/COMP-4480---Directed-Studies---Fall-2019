"""
Quick program to rmove crimes without positional data
"""
import utm
import numpy
from decimal import Decimal

source_file = open('Crimes_with_location_goodtimestamp_gps.csv', 'r')

crime_destination = open('Crimes_with_location_b_and_e_gps_goodtimestamp.csv', 'w')


# Read first line
line = source_file.readline()

# Write to the two files
crime_destination.write(line)

# Read first line of actual data
line = source_file.readline()
count = 1

while line:
    split_line = line.split(',')
    
    if (split_line[0])[0:5] == 'Break':
        crime_destination.write(line)

    # continue reading lines till done
    line = source_file.readline()

    # Print update every 10000 rows proccessed
    if count % 10000 == 0:
        print(count)
        
    count += 1

# Close all files
source_file.close()
crime_destination.close()


## >>> utm.to_latlon(494285.25,5453254.66, 10, 'U')
