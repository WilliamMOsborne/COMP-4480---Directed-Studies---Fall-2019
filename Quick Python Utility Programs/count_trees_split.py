"""
Quick program to count number of street light poles near a location
"""

source_file = open('tree-locations.csv', 'r')

destination = open('tree-locations-01.csv', 'w')


# Read first line
line = source_file.readline()
# Write header to the file
destination.write('UTM_X' + ',' + 'UTM_Y' + '\n')

# Read first line of actual data
line = source_file.readline()
count = 1

while line:
    line = line.replace('"', '')
    split_line = line.split(',')

    # Print all data to new line
    destination.write(split_line[0] + ',' + split_line[1])

    # continue reading lines till done
    line = source_file.readline()

    # Print update every 10000 rows proccessed
    if count % 10000 == 0:
        print(count)
        
    count += 1

    

# Close all files
source_file.close()
destination.close()

