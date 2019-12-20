# Editing Sunrise and Sunset Data


files = ["2003 Vancouver Sunrise-Set.txt",
         "2004 Vancouver Sunrise-Set.txt",
         "2005 Vancouver Sunrise-Set.txt",
         "2006 Vancouver Sunrise-Set.txt",
         "2007 Vancouver Sunrise-Set.txt",
         "2008 Vancouver Sunrise-Set.txt",
         "2009 Vancouver Sunrise-Set.txt",
         "2010 Vancouver Sunrise-Set.txt",
         "2011 Vancouver Sunrise-Set.txt",
         "2012 Vancouver Sunrise-Set.txt",
         "2013 Vancouver Sunrise-Set.txt",
         "2014 Vancouver Sunrise-Set.txt",
         "2015 Vancouver Sunrise-Set.txt",
         "2016 Vancouver Sunrise-Set.txt",
         "2017 Vancouver Sunrise-Set.txt",
         "2018 Vancouver Sunrise-Set.txt",
         "2019 Vancouver Sunrise-Set.txt" ]

destination = open('Daylight_2003_2019_fixed.csv', 'w')

year = 2003
seperator = ','

for file in files:
    source_file = open(file, 'r')

    # read down to data
    for i in range(0,20):
        line = source_file.readline()    
    
    while line:
        split_line = line.split() # split by whitespace

        if split_line[0] == 'Jan':
            month = '01'
        elif split_line[0] == 'Feb':
            month = '02'
        elif split_line[0] == 'Mar':
            month = '03'
        elif split_line[0] == 'Apr':
            month = '04'
        elif split_line[0] == 'May':
            month = '05'
        elif split_line[0] == 'Jun':
            month = '06'
        elif split_line[0] == 'Jul':
            month = '07'
        elif split_line[0] == 'Aug':
            month = '08'
        elif split_line[0] == 'Sep':
            month = '09'
        elif split_line[0] == 'Oct':
            month = '10'
        elif split_line[0] == 'Nov':
            month = '11'
        elif split_line[0] == 'Dec':
            month = '12'

        day = split_line[1]
        if len(day) < 2:
            day = '0' + split_line[1]
       

        destination.write(str(year) + '-' + month + '-' + day + ',') 
        destination.write(seperator.join(split_line) + '\n')
        line = source_file.readline()

    source_file.close()
    print('Done file')
    year += 1

print('Done All')
destination.close()
    
