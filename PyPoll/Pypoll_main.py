import os
import csv

poll = {}
total_votes = 0
candidates = []
num_votes = []
percent = []
winner_list = []

file = os.path.join('Resources/election_data.csv')
with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader, None)

    for row in csvreader:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1

for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

for n in num_votes:
    percent.append(round(n/total_votes*100, 3))

clean_data = list(zip(candidates, num_votes, percent))

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

winner = winner_list[0]

if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

output_file = os.path.join('election_results.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

with open(output_file, 'r') as readfile:
    print(readfile.read())