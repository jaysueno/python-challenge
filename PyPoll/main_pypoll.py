import os
import csv

# define file path
poll_csv = os.path.join('Resources', 'election_data.csv')
poll_output_file = os.path.join('Analysis', 'PyPoll_output_file.txt')
print(poll_csv)

# define variables
total_votes = 0
candidates = [] # empty list that we will ammend with candidates
votes = [int(0), int(0), int(0), int(0)] # list of place holders for candidate votes
vote_percentages =[float(0), float(0), float(0), float(0)] # list placeholders for candidate percentages

# Open data file with a csv reader and skip the header
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(csvreader)
    #start the for loop
    for row in csvreader:
        # Calculate total votes with a counter
        total_votes += 1
        # use a conditional statement to find unique candidate names to append into the candidates list.
        if row[2] not in candidates: 
            candidates.append(row[2])
csvfile.close()

with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(csvreader)
    # Start another for loop.
    for row in csvreader:
        # Vote counter for each candidate. If the index name matches the row, then add it to the corresponding votes list index.
        if row[2] == candidates[0]:
            votes[0] = votes[0] + 1
        elif row[2] == candidates[1]:
            votes[1] = votes[1] + 1
        elif row[2] == candidates[2]:
            votes[2] = votes[2] + 1
        elif row[2] == candidates[3]:
            votes[3] = votes[3] + 1

# Calculations - Vote percentages of each candidate. Assign the value to an index of vote percentages. Format the votes
vote_percentages[0] = candidate0_percentage = {'{:.3f}%'.format((votes[0] / total_votes) * 100)}
vote_percentages[1] = candidate1_percentage = {'{:.3f}%'.format((votes[1] / total_votes) * 100)}
vote_percentages[2] = candidate2_percentage = {'{:.3f}%'.format((votes[2] / total_votes) * 100)}
vote_percentages[3] = candidate3_percentage = {'{:.3f}%'.format((votes[3] / total_votes) * 100)}

# Find the winner by finding the max() within the votes list and then pulling the same index from the candidates list.
winner_int = votes.index(max(votes))
winner = candidates[winner_int]

# Print results in terminal and onto PyPoll_output_file.txt file in the analysis folder
with open(poll_output_file, 'w') as txt_file:
    output_string = ("Election Results \n"
                    "-------------------------\n"
                    f"Total Votes: {total_votes}\n"
                    "-------------------------\n"
                    f"{candidates[0]}: {candidate0_percentage} ({votes[0]})\n"
                    f"{candidates[1]}: {candidate1_percentage} ({votes[1]})\n" 
                    f"{candidates[2]}: {candidate2_percentage} ({votes[2]})\n" 
                    f"{candidates[3]}: {candidate3_percentage} ({votes[3]})\n" 
                    "-------------------------\n"
                    f"Winner: {winner}\n"
                    "-------------------------\n"
                    )
    txt_file.write(output_string)
print(output_string)