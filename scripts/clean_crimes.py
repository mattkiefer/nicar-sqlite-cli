# IPython log file
import pdb

import csv
crimes = open('crime.csv','r')
crime_headers = ['crimeDate','crimeTime','crimeCode','location','description','weapon','post','district','neighborhood'] 
crime_csv = csv.DictReader(crimes,crime_headers)
# crime_csv = [x for x in crime_csv]
crime_csv_2 = csv.DictWriter(open('crimes2.csv','w'),crime_headers)
for line in crime_csv:
    line['neighborhood'] = line['neighborhood'].lower()
    crime_csv_2.writerow(line)
    print line    

crimes.close()
