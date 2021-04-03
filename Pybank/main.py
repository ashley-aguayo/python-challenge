import os
import csv
#set file path
csvpath = r'C:\Users\ashle\python-challenge\Pybank\resources\budget_data.csv'
#set variables
total_months = 0
total_amount = 0
total_change = 0
Average_change= 0
Greatest_increase = 0
Greatest_decrease = 0
previous_amount = 0
net_change_list = []

#open file with csv reader
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #check the column headers
    print(csvreader)
    csv_header = next(csvreader)
    print(f"csv header: {csv_header}")
    first_row = next(csvreader)
    total_months = total_months + 1 
    amount = float(first_row[1])
    total_amount = total_amount + amount
    previous_amount = amount
    total_change = 0
    #confirm rows
    for row in csvreader:
        #print(row)
    #create variables needed for financial analysis    
        date = str(row[0])
        amount = float(row[1])
        
#Total Months
        total_months = total_months + 1 
        #print(total_months)
#Total Amount in Profit and Losses
        total_amount = total_amount + amount
        #print(total_amount)
#Greatest increase in profits
        if Greatest_increase < amount - previous_amount: 
            Greatest_increase = amount - previous_amount
        #print(Greatest_increase)
        if Greatest_decrease > amount - previous_amount:
            Greatest_decrease = amount - previous_amount
        
        net_change_list.append(amount - previous_amount)
        Average_change = sum(net_change_list) / len(net_change_list)
        #print(total_change)
        previous_amount = amount

print(Greatest_decrease)
print(Greatest_increase)
print(sum(net_change_list))
print(Average_change)    
#create output file with results
with open(r'C:\Users\ashle\python-challenge\Pybank\anaylysis\financial_analysis.txt', 'w', newline='') as txtfile:
    txtfile.write(f'Financial Analysis\n---------------------------')
    txtfile.write(f'\n Total Months: {len(net_change_list)}\n Total: ${total_amount} \n Greatest Increase in Profits: (${Greatest_increase}) \n Greatest Decrease in Profits: (${Greatest_decrease})')




