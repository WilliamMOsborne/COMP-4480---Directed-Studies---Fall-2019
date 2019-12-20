"""
Quick program to rmove crimes without positional data
"""
import utm
import numpy
import re


source_file = open('street-lighting-poles.csv', 'r')

destination = open('street_lights_processed.csv', 'w')

seperator = ','

# Read first line
line = source_file.readline()

# Write the first line
destination.write(line)

# Read first line of actual data
line = source_file.readline()

count = 1

while line:
    
    split_line = line.split(',')
#44
    latitude = (split_line[2])[60:]
    print(latitude)
    longitude = (split_line[3])[1:]
    longitude = longitude[:-2]
    print(longitude)
    
    utm_coords = utm.from_latlon(float(split_line[2]), float(split_line[3]))

    line = str(utm_coords[0]) + ',' + str(utm_coords[1]) + ',' + line

    destination.write(line)

    # continue reading lines till done
    line = source_file.readline()

    line = line.replace('{"type": "Point", "coordinates": [', '')
    line = line.replace('{]}', '')

    # Print update every 10000 rows proccessed
    if count % 10000 == 0:
        print(count)
        
    count += 1



# Close all files
source_file.close()
destination.close()


## >>> utm.to_latlon(494285.25,5453254.66, 10, 'U')
