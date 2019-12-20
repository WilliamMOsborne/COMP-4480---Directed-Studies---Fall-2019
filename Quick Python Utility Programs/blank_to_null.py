"""
Quick program to rmove crimes without positional data
"""

source_file = open('Vancouver_Airport_Weather_Hourly.csv', 'r')

destination = open('Vancouver_Airport_Weather_Hourly_NULLS.csv', 'w')


# Read first line
line = source_file.readline()

# Write the first line (Header)
destination.write(line)


# Read first line of actual data
line = source_file.readline()
count = 1

while line:

    newline = line.replace(',,', ',NULL,')
    destination.write(newline)
    # continue reading lines till done
    line = source_file.readline()

    # Print update every 10000 rows proccessed
    if count % 10000 == 0:
        print(count)
        
    count += 1

# Close all files
source_file.close()
destination.close()

