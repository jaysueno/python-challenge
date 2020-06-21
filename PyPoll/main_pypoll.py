import os
import csv
import pandas as pd

# define file path
poll_csv = os.path.join('Resources', 'election_data.csv')
poll_output_file = os.path.join('Analysis', 'PyPoll_output_file.txt')
print(poll_csv)

# define variables
total_votes = 0
candidates = []
votes = [int(0), int(0), int(0), int(0)]
vote_percentages =[float(0), float(0), float(0), float(0)]

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(csvreader)

    #start the for loop
    for row in csvreader:

#   * The total number of votes cast
        total_votes += 1


#   * A complete list of candidates who received votes
        if row[2] not in candidates: 
            candidates.append(row[2])
        #     # ['Khan', 'Correy', 'Li', "O'Tooley"]
        #     #manipulate the candidates list outside of the for loop
        # break
# print(candidates[1])
csvfile.close()

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(csvreader)
# for row in csvreader:
    for row in csvreader:

    # for row in csvreader:

        if row[2] == candidates[0]:
            votes[0] = votes[0] + 1
        elif row[2] == candidates[1]:
            votes[1] = votes[1] + 1
        elif row[2] == candidates[2]:
            votes[2] = votes[2] + 1
        elif row[2] == candidates[3]:
            votes[3] = votes[3] + 1

#Calculations
#   * The percentage of votes each candidate won
vote_percentages[0] = candidate0_percentage = votes[0] / total_votes
vote_percentages[1] = candidate1_percentage = votes[1] / total_votes
vote_percentages[2] = candidate2_percentage = votes[2] / total_votes
vote_percentages[3] = candidate3_percentage = votes[3] / total_votes
print (vote_percentages)
print(candidates)
  
# print (votes)     

# track all the votes associated with each candidate using a list or a dictionary
        
#clue - look at a counter maybe? in or not in a list. if row[2] == candidate: do a count
#   * The total number of votes each candidate won
print (total_votes) 
#   * The winner of the election based on popular vote.
winner_int = max(vote_percentages)
print(candidates[int(winner_int)])
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

# Jay Sueno  5:09 PM
# hello! yes. i'm on the part where i can pull the names of the candidates. now i need to figure out how to create a list or dictionary of some sort to assign number of votes. how far have you gotten?





# 5:09
# i decided not to use pandas in this exercise so it's a little bit more challenging for me.

# Minerva Banuelos  6:24 PM
# I submitted it last night. I think Thompson asked about using pandas...but even so we use pandas for the next homework.
# Referring to exercises, "02-Ins_Dicts" and "06-Evr_List_Comprehensions" from the 3rd session helps with the basics. Let me see which other example helped me with that part...hang on!
# :heart:
# 1

# 6:25
# Sorry, I just got home and saw your messages.

# Minerva Banuelos  6:52 PM
# For dictionary, a good reference: "03-Stu_HobbyBook"
# For conditional statements: "07-In_Conditionals" + "08-Stu_ConditionalConundrum"
# :heart:
# 1

