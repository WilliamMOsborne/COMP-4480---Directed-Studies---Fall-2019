"""
Quick program to rmove crimes without positional data
"""
import utm
import numpy
import re


source_file = open('street_trees_partly_processed.csv', 'r')

destination = open('street_trees_processed.csv', 'w')

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

    new_line = []    

    new_line.append(split_line[0])
    new_line.append(split_line[1])
    

    # extract gps coords
    gps = split_line[2]
    gps_lat = gps[62:79]
    gps_long = gps[41:60]
    

    print(gps_lat)
    print(gps_long)
    new_line.append(gps_lat)
    new_line.append(gps_long)

    utm_coords = utm.from_latlon(float(gps_lat), float(gps_long))

    new_line.append(str(utm_coords[0]))
    new_line.append(str(utm_coords[1]))

    new_line.append(split_line[3])

    new_line = seperator.join(new_line)

    destination.write(new_line)

    # continue reading lines till done
    line = source_file.readline()

    # Print update every 10000 rows proccessed
    if count % 10000 == 0:
        print(count)
        
    count += 1

"""

# Close all files
source_file.close()
destination.close()


## >>> utm.to_latlon(494285.25,5453254.66, 10, 'U')
