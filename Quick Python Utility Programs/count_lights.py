"""
Quick program to count number of street light poles near a location
"""

source_file = open('Vancouver_Crimes.csv', 'r')
light_source = open('FixedLights.csv', 'r')

destination = open('Crimes_with_light_count.csv', 'w')


# Read first line
line = source_file.readline()
# Write header to the file
destination.write(line)

# Read first line of actual data
line = source_file.readline()
count = 1

while line:
    split_line = line.split(',')

    # Read first Line (Header) of Light Data
    light_line = light_source.readline()

    # Read first line of light_pole data
    light_line = light_source.readline()

    light_count = 0 # reset light count to 0

    crime_X_coord = float(split_line[9])
    crime_Y_coord = float(split_line[10])
    
    # Loop through light_pole file to count number of poles at location
    while light_line:
        split_light_line = light_line.split(',')

        light_X_coord_less = float(split_light_line[2]) - 12.5
        light_X_coord_more = float(split_light_line[2]) + 12.5
        
        light_Y_coord_less = float(split_light_line[3]) - 12.5
        light_Y_coord_more = float(split_light_line[3]) + 12.5

        # compare UTM or crime to utm of light + and - 12.5m (so 25 meter cube)
        if (crime_X_coord > light_X_coord_less) and (crime_X_coord < light_X_coord_more) and (crime_Y_coord > light_Y_coord_less) and (crime_Y_coord < light_Y_coord_more):
            light_count = light_count + 1

        # Read next line of light_pole data
        light_line = light_source.readline()
        

    # Finished one row of crime data, so read the next
    light_line = light_source.readline()

    # Print all data to new line
    destination.write(str(light_count) + ',' + line)

    # continue reading lines till done
    line = source_file.readline()

    # Print update every 10000 rows proccessed
    if count % 10000 == 0:
        print(count)
        
    count += 1

    # Reset Light Source file to its start to search through again
    light_source.seek(0)

    

# Close all files
source_file.close()
light_source.close()
destination.close()

