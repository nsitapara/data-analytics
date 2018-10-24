
## PyPoll

# ![Vote-Counting](Images/Vote_counting.jpg)

# * In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

# * You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

#   * The total number of votes cast

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

import csv
import os
import pandas as pd
import numpy as np



budget_data_file =  os.path.abspath(r"C:\Users\nsita\Dropbox\UCB\data-analytics\Homework\Homework 3\PyPoll\Resources\election_data.csv")
# budget_data_file =  os.path.abspath(r"C:\Users\NS\Dropbox\UCB\data-analytics\Homework\Homework 3\PyPoll\Resources\election_data.csv")

with open(budget_data_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    counter = 0
    names = []
    county = []
    for row in csvreader:
        county.append(row[1])
        names.append(row[2])
    names = set(names)
    county = set(county)
    # print(county)
    # print(names)


dict = {}
# print(dict)

def loopThroughNames(budget_data_file, name):
    with open(budget_data_file, newline='') as csvfile:
        votetotal = 0
        csvreader = csv.reader(csvfile, delimiter=',')
        for row in csvreader:
            if str(row[2]) == str(name):
                votetotal += 1
        dict[name] = votetotal

for name in names:
    loopThroughNames(budget_data_file, name)

# with open(budget_data_file, newline='') as csvfile:
#     # print(csvreader)
#     votetotal = 0
#     for name in names:
#         csvreader = csv.reader(csvfile, delimiter=',')
#         for row in csvreader:
#             if str(row[2]) == str(name):
#                 votetotal += 1
#         dict[name] = votetotal
#         csvfile.seek(0,0)
#     votetotal = 0
# print(dict)

# dict = {'Correy': 704200, "O'Tooley": 809830, 'Khan': 3028061, 'Li': 3521001}

allvotes = 0
for key in dict:
    allvotes = allvotes + dict[key]

print(allvotes)
result = {}
winner_per = 0
for key in dict:
    percentage = dict[key]/allvotes 
    result[key]= percentage
    if percentage > winner_per:
        winner_per = percentage
        winner_name = key
    

print(result)


print("Election results\n")
print("-------------------\n")
print("Total Votes:" + str(allvotes) + "\n")
print("-------------------\n")
for items in result:
    print(items + ": "+ "{:.3%}".format(result[items]))
print("-------------------\n")

print("Winner: " + winner_name)
print("-------------------\n")

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
 

# # Write output to file called output.txt
# text_file = open('Output.txt', 'w')
# text_file.write("Financial Analysis\n")
# text_file.write("--------------------\n")
# text_file.write("Total Months:" + str(totalmonths_counter) + "\n")
# text_file.write("Total:" + str(total) + "\n")
# text_file.write("Greatest Increase in Profits: " + str(IncreaseProfit_Date) + "($" + str(IncreaseProfit) + ")\n")
# text_file.write("Greatest Decrease in Profits: " + str(DecreaseProfit_Date) + "($" + str(DecreaseProfit) + ")") 
# text_file.close()