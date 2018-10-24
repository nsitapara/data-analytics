#
#
# * Your task is to create a Python script that analyzes the records to calculate each of the following:
#
#   * The total number of months included in the dataset
#
#   * The total net amount of "Profit/Losses" over the entire period
#
#   * The average change in "Profit/Losses" between months over the entire period
#
#   * The greatest increase in profits (date and amount) over the entire period
#
#   * The greatest decrease in losses (date and amount) over the entire period
#
# * As an example, your analysis should look similar to the one below:
#
#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```
#
# * In addition, your final script should both print the analysis to the terminal and export a text file with the results.

import csv
import os

# budget_data_file =  os.path.abspath(r"C:\Users\NS\Dropbox\UCB\data-analytics\Homework\Homework 3\PyBank\Resources\budget_data.csv")
budget_data_file = os.path.join("PyBank", "Resources", "budget_data.csv")

with open(budget_data_file, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # print(csvreader)
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    totalmonths_counter = 0
    total = 0
    IncreaseProfit = 0
    DecreaseProfit = 0
    # Read each row of data after the header
    for row in csvreader:
        #conditional to find the highest increase in profit and decrease in profit
        if int(row[1]) > IncreaseProfit:
            IncreaseProfit =int(row[1])
            # print("CHANGE IN INCREASE PROFIT TO:" ,IncreaseProfit)
            IncreaseProfit_Date = str(row[0])

        if int(row[1]) < DecreaseProfit:
                DecreaseProfit =int(row[1])
                # print("CHANGE IN DECREASE PROFIT TO:" ,DecreaseProfit)
                DecreaseProfit_Date = str(row[0])  
        # print(row)|
        total = total + int(row[1])
        totalmonths_counter += 1

        
    ##Values are different, are the same if change the values in the cells. different data set?
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)    

print("Financial Analysis")
print("--------------------")
print("Total Months:", totalmonths_counter)
print("Total: ",total)
AverageChange = total / totalmonths_counter
print("Average  Change: ", AverageChange)
print("Greatest Increase in Profits: ", IncreaseProfit_Date,"($", IncreaseProfit, ")")
print("Greatest Decrease in Profits: ", DecreaseProfit_Date,"($", DecreaseProfit, ")") 

# Write output to file called output.txt
text_file = open('Output.txt', 'w')
text_file.write("Financial Analysis\n")
text_file.write("--------------------\n")
text_file.write("Total Months:" + str(totalmonths_counter) + "\n")
text_file.write("Total:" + str(total) + "\n")
text_file.write("Greatest Increase in Profits: " + str(IncreaseProfit_Date) + "($" + str(IncreaseProfit) + ")\n")
text_file.write("Greatest Decrease in Profits: " + str(DecreaseProfit_Date) + "($" + str(DecreaseProfit) + ")") 
text_file.close()