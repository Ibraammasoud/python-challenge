# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:20:30 2024

@author: Ibraam Masoud
"""

import csv
import os


file_to_load = os.path.join("Resources", "/Resources/budget_data.csv")  
file_to_output = os.path.join("analysis", "/analysis/budget_analysis.txt")  

total_months = 0
total_net = 0
previous_month_profit = 0
net_change_list = []
greatest_increase = {"month": "", "amount": 0}
greatest_decrease = {"month": "", "amount": 0}


with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

   
    header = next(reader)

    
   
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_month_profit = int(first_row[1])
  
    for row in reader:
        total_months += 1
        total_net += int(row[1])
        current_month_profit = int(row[1])
        
       
        net_change = current_month_profit - previous_month_profit
        net_change_list.append(net_change)
        previous_month_profit = current_month_profit

        
        if net_change > greatest_increase["amount"]:
            greatest_increase["amount"] = net_change
            greatest_increase["month"] = row[0]

       
        if net_change < greatest_decrease["amount"]:
            greatest_decrease["amount"] = net_change
            greatest_decrease["month"] = row[0]


average_net_change = sum(net_change_list) / len(net_change_list)


output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Losses: {greatest_decrease['month']} (${greatest_decrease['amount']})\n"
)


print(output)


with open(file_to_output, "w") as txt_file:
    txt_file.write(output)