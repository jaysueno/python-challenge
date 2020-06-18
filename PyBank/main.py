import os
import csv

# define file path
bank_csv = os.path.join("Resources", "budget_data.csv")
print(bank_csv)

# define variables
date = bank_csv[0]
pl = bank_csv[1]
total_months = 0
total_profit_loss = 0
average_pl = 0
greatest_inc = 0
greatest_dec = 0

# Read in the CSV file
with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(bank_csv, delimiter=",")

# The total number of months included in the dataset
csvreader[0]
#mThe net total amount of "Profit/Losses" over the entire period

# The average of the changes in "Profit/Losses" over the entire period

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in losses (date and amount) over the entire period
