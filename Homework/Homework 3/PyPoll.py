import csv
import os

# budget_data_file =  os.path.abspath(r"C:\Users\nsita\Dropbox\UCB\data-analytics\Homework\Homework 3\PyPoll\Resources\election_data.csv")
# budget_data_file =  os.path.abspath(r"C:\Users\NS\Dropbox\UCB\data-analytics\Homework\Homework 3\PyPoll\Resources\election_data.csv")
budget_data_file =  os.path.join("PyPoll", "Resources", "election_data.csv")

dict = {}
with open(budget_data_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")
    counter = 0
    names = []
    county = []
    for row in csvreader:
        if row[2] in dict:
            dict[row[2]] = dict[row[2]] + 1
        else:
            dict[row[2]] = 1
    print(dict)

#Count the total number of votes by using a forloop and a variable to keep track of sum
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

# # # Write output to file called Part2_Output.txt
text_file = open('Part2_Output.txt', 'w')
text_file.write("Election results\n")
text_file.write("-------------------\n")
text_file.write("Total Votes:" + str(allvotes) + "\n")
text_file.write("-------------------\n")
for items in result:
    text_file.write(items + ": "+ "{:.3%}".format(result[items]) + "\n")
text_file.write("-------------------\n")
text_file.write("Winner: " + winner_name + "\n")
text_file.write("-------------------\n")
text_file.close()