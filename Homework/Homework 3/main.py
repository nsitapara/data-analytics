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

   
def printandwrite(message):
    print(message)
    text_file.write(message)


# Write output to file called output.txt
text_file = open('Output.txt', 'w')
printandwrite("Financial Analysis\n")
printandwrite("--------------------\n")
printandwrite("Total Months:" + str(totalmonths_counter) + "\n")
printandwrite("Total:" + str(total) + "\n")
AverageChange = total / totalmonths_counter
printandwrite("Average  Change: " +str(AverageChange) + "\n")
printandwrite("Greatest Increase in Profits: " + str(IncreaseProfit_Date) + "($" + str(IncreaseProfit) + ")\n")
printandwrite("Greatest Decrease in Profits: " + str(DecreaseProfit_Date) + "($" + str(DecreaseProfit) + ")") 
text_file.close()