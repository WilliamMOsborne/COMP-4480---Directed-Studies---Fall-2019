"""
Quick program to rmove crimes without positional data
"""

source_file = open('crime_csv_all_years.csv', 'r')

crime_destination = open('Crimes_with_location.csv', 'w')
no_location_destination = open('Crimes_without_location.csv', 'w')

# Read first line
line = source_file.readline()

# Write to the two files
crime_destination.write(line)

no_location_destination.write(line)

# Read first line of actual data
line = source_file.readline()
count = 1

while line:
    split_line = line.split(',')
    if float(split_line[9]) != 0.0:
        crime_destination.write(line)
    else:
        no_location_destination.write(line)

    # continue reading lines till done
    line = source_file.readline()

    # Print update every 10000 rows proccessed
    if count % 10000 == 0:
        print(count)
        
    count += 1

# Close all files
source_file.close()
crime_destination.close()
no_location_destination.close()
