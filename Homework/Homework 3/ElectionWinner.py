import csv
import os

budget_data_file =  os.path.abspath(r"C:\Users\nsita\Dropbox\UCB\data-analytics\Homework\Homework 3\PyPoll\Resources\election_data.csv")
budget_data_file =  os.path.abspath(r"C:\Users\NS\Dropbox\UCB\data-analytics\Homework\Homework 3\PyPoll\Resources\election_data.csv")
budget_data_file =  os.path.join("PyPoll", "Resources", "election_data.csv")
text_file = open('Part2_Output.txt', 'w')
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
#to calculate the percentage for each candidiate
for key in dict:
    percentage = dict[key]/allvotes 
    result[key]= percentage
    if percentage > winner_per:
        winner_per = percentage
        winner_name = key
   
print(result)


#method to print and write out the message
def printandwrite(message):
    print(message)
    text_file.write(message)

#calling the method with the inputs
printandwrite("Election results\n")
printandwrite("-------------------\n")
printandwrite("Total Votes:" + str(allvotes) + "\n")
printandwrite("-------------------\n")
for items in result:
    printandwrite(items + ": "+ "{:.3%}".format(result[items])+"\n")
printandwrite("-------------------\n")

printandwrite("Winner: " + winner_name + "\n")
printandwrite("-------------------\n")
