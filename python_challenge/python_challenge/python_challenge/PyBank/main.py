
import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

months_value = []
profit_loss_value = []
profit_loss_change = []

print("Financial Analysis")
print("-------------------------------")

with open(budget_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvreader)
   

    for row in csvreader:
     months_value.append(row[0])
     profit_loss_value.append(int(row[1]))
   
    months_total = len(months_value)
    print(f"Total Months:", months_total)
     
    profit_loss_total = sum(profit_loss_value)
    print(f"Total: ${profit_loss_total}")


    #The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(1, len(profit_loss_value)):
        profit_loss_change.append((int(profit_loss_value[i]) - int(profit_loss_value[i-1])))
    
    change_average = sum(profit_loss_change) / len(profit_loss_change)
    change_average = round(change_average, 2)
    
    print(f"Average Change: ${change_average}")
    
    greatest_increase = max(profit_loss_change)
    greatest_decrease = min(profit_loss_change)
    
    print(f"Greatest Increase in Profits: {months_value[profit_loss_change.index(greatest_increase) + 1]} (${greatest_increase})")
    print(f"Greatest Decrease in Profits: {months_value[profit_loss_change.index(greatest_decrease) + 1]} (${greatest_decrease})")
    
    #Export a text file with the results

    with open("text_file.txt", "w") as file:
        file.write("Financial Analysis\n")
        file.write("-------------------------------\n")
        file.write(f"Total Months: {months_total}\n")
        file.write(f"Total: ${profit_loss_total}\n")
        file.write(f"Average Change: ${change_average}\n")
        file.write(f"Greatest Increase in Profits: {months_value[profit_loss_change.index(greatest_increase) + 1]} (${greatest_increase})\n")
        file.write(f"Greatest Decrease in Profits: {months_value[profit_loss_change.index(greatest_decrease) + 1]} (${greatest_decrease})\n")
