import os
import csv

# define file path
bank_csv = os.path.join('Resources', 'budget_data.csv')
#print(bank_csv)
# define variables
total_months = 0
total_profit_loss = 0
greatest_inc = 0
#monthly_change = []
greatest_dec = 0

# Read in the CSV file
with open(bank_csv , 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(csvreader)

 
# start the loop
    for row in csvreader: #can also use line
# The total number of months included in the dataset
        total_months = total_months + 1
        #print(total_months)
# The net total amount of "Profit/Losses" over the entire period
        total_profit_loss += int(row[1])

# The average of the changes in "Profit/Losses" over the entire period
        #store all the numbers in a list; count the length of the list; then use a function 'def (pl_avg)' to output and "call" a value
        average_pl = total_profit_loss / total_months
        #print(row[1])
#print(average_pl)
#print(total_profit_loss)
#print(total_months)
# The greatest increase in profits (date and amount) over the entire period
        #start with the greatest_inc = 0 then with each line, if row[1] > greatest_inc: greatest_inc = row[1]
        if float(row[1]) > greatest_inc:
                greatest_inc = float(row[1])
                greatest_inc_date = row[0]
#print(greatest_inc_date)
#print(greatest_inc)
# The greatest decrease in losses (date and amount) over the entire period
         #start with the greatest_inc = 0 then with each line, if row[1] > greatest_inc: greatest_inc = row[1]
        if float(row[1]) < greatest_dec:
                greatest_dec = float(row[1])
                greatest_dec_date = row[0]

print(greatest_dec)
print(greatest_dec_date)