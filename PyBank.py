# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:20:30 2024

@author: Ibraam Masoud
"""

# Dependencies
import csv
import os


file_to_load = os.path.join("Resources", "C:/Users/Ibraam Masoud/Desktop/BootCamp/challange 3/Starter_Code/PyBank/Resources/budget_data.csv")  
file_to_output = os.path.join("analysis", "C:/Users/Ibraam Masoud/Desktop/BootCamp/challange 3/Starter_Code/PyBank/Resources/budget_analysis.txt")  

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_month_profit = 0
net_change_list = []
greatest_increase = {"month": "", "amount": 0}
greatest_decrease = {"month": "", "amount": 0}
# Add more variables to track other necessary financial data

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    
    # Extract the first row to initialize the previous_month_profit
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_month_profit = int(first_row[1])
    # Process each row of data
    for row in reader:
        total_months += 1
        total_net += int(row[1])
        current_month_profit = int(row[1])
        
        # Track the net change
        net_change = current_month_profit - previous_month_profit
        net_change_list.append(net_change)
        previous_month_profit = current_month_profit

        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase["amount"]:
            greatest_increase["amount"] = net_change
            greatest_increase["month"] = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease["amount"]:
            greatest_decrease["amount"] = net_change
            greatest_decrease["month"] = row[0]

# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Losses: {greatest_decrease['month']} (${greatest_decrease['amount']})\n"
)

# Print the output
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)