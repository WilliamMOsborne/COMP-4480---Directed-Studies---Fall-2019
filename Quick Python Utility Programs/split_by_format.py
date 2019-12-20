"""
 Quick script to separate the different formats of data from court data


Manually changing file names for:
From:
CourBC_Vancouver_Law_Courts.csv - done
CourBC_Vancouver_Law_Courts_SC.csv - already only one format
CourBC_Vancouver_Provincial_Court.csv - done
CourBC_Vancouver_Provincial_Court_SC.csv - done
"""

source_file = open('CourBC_Vancouver_Provincial_Court_SC.csv', 'r')

list_destination = open('CourBC_Vancouver_Provincial_Court_SC-list.csv', 'w')
date_destination = open('CourBC_Vancouver_Provincial_Court_SC-date.csv', 'w')

# Read first line
line = source_file.readline()

# Write to the two files
list_destination.write(line)

date_destination.write(line)

# Read first line of actual data
line = source_file.readline()
count = 1

while line:
    if line[0] == 'l':
        list_destination.write(line)
    else:
        date_destination.write(line)

    # continue reading lines till done
    line = source_file.readline()

    # Print update every 10000 rows proccessed
    if count % 10000 == 0:
        print(count)
        
    count += 1

# Close all files
source_file.close()
list_destination.close()
date_destination.close()
