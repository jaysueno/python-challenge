import os
import csv

# define file path
bank_csv = os.path.join('Resources', 'budget_data.csv')
bank_output_file = os.path.join('Analysis', 'PyBank_output_file.txt')
#print(bank_csv)

# define variables
total_months = [] #we need this list for an index value of the max/min
total_profit_loss = 0 #this is a sum of all the p/l
# greatest_inc = 0 #no longer needed because this should be 
# greatest_dec = 0 
profit_loss_delta = [] #need this to be a list of differences between each day. to capture use an append

# Read in the CSV file
with open(bank_csv , 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") #make sure that your referencing the proper variables/files
    header = next(csvreader)
    print(csvreader)
 
    # start the for loop
    for row in csvreader: #can also use line

        # The total number of months included in the dataset
        total_months = total_months + 1

        # The net total amount of "Profit/Losses" over the entire period
        total_profit_loss += int(row[1])

        # The average of the changes in "Profit/Losses" over the entire period. make sure we do one less 
        average_pl = total_profit_loss / total_months

        # The greatest increase in profits (date and amount) over the entire period
        #start with the greatest_inc = 0 then with each line, if row[1] > greatest_inc: greatest_inc = row[1]
        if float(row[1]) > greatest_inc:
                greatest_inc = float(row[1]) #make sure both values are float types due to decimal points
                greatest_inc_date = row[0]

        # The greatest decrease in losses (date and amount) over the entire period
        #start with the greatest_dec = 0 then with each line, if row[1] < greatest_dec: greatest_dec = row[1]
        if float(row[1]) < greatest_dec:
                greatest_dec = float(row[1]) #make sure both values are float types due to decimal points
                greatest_dec_date = row[0]

# print (int(greatest_dec))
# print (int(greatest_inc))
# print (round(average_pl, 2))
# print (int(total_profit_loss))

output = (
        f"Financial Analysis\n"
        f"----------------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: {'${}'.format(total_profit_loss)}\n"
        f"Average Change: {'${}'.format(round(average_pl, 2))}\n"
        f"Greatest Increase in Profits: {greatest_inc_date} ({'${}'.format(int(greatest_inc))})\n"
        f"Greatest Decrease in Profits: {greatest_dec_date} ({'${}'.format(int(greatest_dec))})\n"
)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
print (output) #prints out to terminal

# with open(bank_output_file, "a") as txt_file: #outputs a .txt file to the Analysis folder
        # txt_file.write(output)


