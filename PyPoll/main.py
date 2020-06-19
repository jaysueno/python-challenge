import os
import csv
import pandas as pd

# define file path
poll_csv = os.path.join('Resources', 'election_data.csv')
poll_output_file = os.path.join('Analysis', 'PyPoll_output_file.txt')
print(poll_csv)

poll_df = pd.read_csv(poll_csv)
poll_df.head(5)

candidates = poll_df["Candidate"].value_counts()
print(candidates)


# define variables
# total_votes = 0
# total_profit_loss = 0
# greatest_inc = 0
# greatest_dec = 0

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# with open(poll_csv, 'r') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")
#     header = next(csvreader)
#     print(csvreader)

    #start the for loop
    # for row in csvreader:

#   * The total number of votes cast
        # total_votes += 1
# print (total_votes)

#   * A complete list of candidates who received votes
        
#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

# * As an example, your analysis should look similar to the one below:

#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.