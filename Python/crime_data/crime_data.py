import csv
import glob
import os
from collections import namedtuple

# CrimeDataPoint = namedtuple('CrimeDataPoint', 'date', 'major_offense')

def get_crime_data():
    crime_data = glob.glob('*.csv')
    for data in crime_data:
        with open(data, 'r') as f:
            f.readline()


class CrimeDataParser:
    @staticmethod
    def get_rows():
        crime_data = glob.glob('*.csv')
        for data in crime_data:
            with open(data, 'r') as f:
                reader = csv.reader(f)
                reader = list(reader)
                headers = reader.pop(0)
                headers = [new_header.casefold().replace(' ', '_') for new_header in headers]

                row_data = []
                for row in reader:
                    row_data.append(dict(zip(headers, row)))
                return row_data

            def highest_crime(row_data):
                for date in row_data:
                    highest_crime = max(row_data.items(), key=lambda c: c[1])
                    print(highest_crime)





print(CrimeDataParser.get_rows())
