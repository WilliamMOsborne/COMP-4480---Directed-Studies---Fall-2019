"""
Quick program to rmove crimes without positional data
"""

source_file = open('Daylight_2003_2019.csv', 'r')

destination = open('Daylight_2003_2019_Rise_Set.csv', 'w')


# Read first line
line = source_file.readline()

# Write the first line (Header)
destination.write(line)


# Read first line of actual data
line = source_file.readline()
count = 1

while line:
    split_line = line.split(',')
    risehour, risemin = split_line[1].split(':')
    sethour, setmin = split_line[2].split(':')

    newline = split_line[0] + ',' + risehour + ',' + risemin + ',' + sethour + ',' + setmin + ',' + split_line[3]
    
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

