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

budget_data_file =  os.path.abspath(r"C:\Users\nsita\Dropbox\UCB\data-analytics\Homework\Homework 3\PyPoll\Resources\election_data.csv")
# budget_data_file =  os.path.abspath(r"C:\Users\NS\Dropbox\UCB\data-analytics\Homework\Homework 3\PyPoll\Resources\election_data.csv")
votecount = 0
# adict = {"county":
#           {"Candidate":
#                  [{"Name":
#                         votecount}]

# }

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
    names = [name for name in names]
    county = [name for name in county]
    # names = names.sort()
    # county = county.sort()
    # county = list(county).sort()
    # sorted_names = sorted(names, key=str.capitalize)
    sorted_names = names
    # sorted_county =sorted(county, key=str.capitalize)
    sorted_county = county

print(sorted_names)
print(sorted_county)

# print(names[2])
# print(county[1])
# adict{sorted_names:{sorted_county:0}}
todict = {}
for count in county:
    for name in names:
        countname = count,name
        todict[count][name][0]= 0

        # dict[str(count)][str(name)]
        # dict[count]
        # print(count, name)


print(todict)
# combonames = 
# combocounty =
dict = {}
# for items in todict:
#     print(items[0])
#     print(items[1])
output= {}
for items in todict:
    output[items[0]][items[1]] = 0

print(output)


# # print adict)
count = 0
# output = [["county", "name", 0 ]]
# print(outp ut)

with open(budget_data_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    





    for row in csvreader:
        counter = 0
        for items in todict:
            # print(items[0])
            # print(items[1])
            if items[0] == row[1] and items[1] == row[2]:
                countname = items[0]
                name = items[1]
                count +=1
                output[countname][name] += 1


                # print("PLUS 1 for" + str(items[0]), str(items[1]))
print(output)
                
            
        




        # lookupcounty = county
        # lookupname= names
        # if adict[lookupcounty][lookupname] in adict:
        #     adict[lookupcounty][lookupname] = 0 + adict[lookupcounty][lookupname] + 1
            
        # else:
        #     adict[lookupcounty][lookupname] = 0 + adict[lookupcounty][lookupname] + 1
         







        
#         if row[1] not in adict_keys:
#             nameOfCandidate = row[2]
#             coutyname = row[1]
#             counter = 0
#             adict_keys[coutyname] = {nameOfCandidate: counter + 1}
#             counter += 1
            
#         else:
#             nameOfCandidate = row[2]
#             if adict_keys[row[1]][nameOfCandidate]:
#             adict_keys[row[1]][nameOfCandidate] = counter + 1
#             adict_keys[row [1]] = {nameOfCandidate: }
#             counter += 1

        
    # print adict_keys)

    # adict{"Marsh":{"Khan" : 4321321}}

        # if row[2] in adict:
        #     adict[row[2]] = adict[row[2]] + 1
        # else:
        #     adict[row[2]] = 1
        
    # print adict)
    # print(county)
    # print(names)
# allvotes = 0
# for key in adict:
#     allvotes = allvotes + adict[key]

# print(allvotes)
# result = {}
# winner_per = 0
# for key in adict:
#     percentage = adict[key]/allvotes 
#     result[key]= percentage
#     if percentage > winner_per:
#         winner_per = percentage
#         winner_name = key
   
# print(result)
# print("Election results\n")
# print("-------------------\n")
# print("Total Votes:" + str(allvotes) + "\n")
# print("-------------------\n")
# for items in result:
#     print(items + ": "+ "{:.3%}".format(result[items]))
# print("-------------------\n")

# print("Winner: " + winner_name)
# print("-------------------\n")

# # # # Write output to file called Part2_Output.txt
# text_file = open('Part2_Output.txt', 'w')
# text_file.write("Election results\n")
# text_file.write("-------------------\n")
# text_file.write("Total Votes:" + str(allvotes) + "\n")
# text_file.write("-------------------\n")
# for items in result:
#     text_file.write(items + ": "+ "{:.3%}".format(result[items]) + "\n")
# text_file.write("-------------------\n")
# text_file.write("Winner: " + winner_name + "\n")
# text_file.write("-------------------\n")
# text_file.close()