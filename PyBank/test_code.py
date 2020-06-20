import os
import csv

csv_file = os.path.join('Resources', 'budget_data.csv')

with open(csv_file, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    # csv_header = next(csvreader)

    csv_header.append("test")
    
    print(f"CSV Header: {csv_header}")
    csv_header = next(csvreader)
    for row in csvreader:
        csvreader.append(row[2]) += 1

        print(row)