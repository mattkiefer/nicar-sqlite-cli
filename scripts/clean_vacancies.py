# IPython log file
import pdb

import csv
vacancies = open('vacancies.csv','r')
vac_csv = csv.DictReader(vacancies,['neighborhood','count'])
vac_csv = [x for x in vac_csv]
vac_csv
vac_csv_2 = csv.DictWriter(open('vacancies2.csv','w'),['neighborhood','count'])
for line in vac_csv:
    line['neighborhood'] = line['neighborhood'].lower()
    vac_csv_2.writerow(line)
    print line    

vacancies.close()
