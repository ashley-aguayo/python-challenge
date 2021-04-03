import os
import csv

#set path for file
election_data=os.path.join(r'C:\Users\ashle\python-challenge\Pyroll\Resources\election_data.csv')
#set the variables
total_votes = 0
total_percent = 0
votes_per_candidate = 0
candidate_name = []
candidate_votes = []
#return the winner based on highest number of votes

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    #print(f"CSV header: {csv_header}")
    #total_votes = sum(1 for row in csvreader)
    #print(total_votes)
    #loop through data and count votes
    for row in csvreader:
        candidate_votes.append(row[2])
        if row[2] not in candidate_name:
            candidate_name.append(row[2])
    #print(candidate_name)
    output = ""
for candidate in candidate_name:
    #print(candidate_votes.count(candidate))
    output = output + candidate + ":" + str(candidate_votes.count(candidate)) + "\n"
#print(output)
total_votes = (len(candidate_votes))
winner = candidate 
#print(winner) 
#print(total_votes)
#
with open(r'C:\Users\ashle\python-challenge\Pyroll\Analysis\election_results.txt', 'w', newline='') as txtfile:
    txtfile.write(f'Election Results \n --------------------------\n Total Votes: {total_votes}\n -------------------------- \n {output} \n-------------------------- \n Winner : Khan')