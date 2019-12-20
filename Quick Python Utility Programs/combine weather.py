"""
Quick program to rmove crimes without positional data
"""
import glob



files = []
for file in glob.glob("*.csv"):
    files.append(file)

destination = open('Combined_Vancouver_Airport_Weather.csv', 'w')

for file in files:
  source_file = open(file, 'r')
  print('Working on file: ', file)
  line = source_file.readline() # remove the header

  line = source_file.readline()
  while line:
    destination.write(line)
    line = source_file.readline()

  source_file.close()

print('Done')
destination.close()

"""
source_file = open('crime_csv_all_years.csv', 'r')

destination = open('Crimes_with_location.csv', 'w')


# Read first line
line = source_file.readline()

# Write to the two files
destination.write(line)

no_location_destination.write(line)

# Read first line of actual data
line = source_file.readline()
count = 1

while line:
    split_line = line.split(',')
    if float(split_line[9]) != 0.0:
        destination.write(line)
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
destination.close()
no_location_destination.close()
"""
