#importing files for program
import csv

#setting variable for csv extraction
bank_path = r"\Users\koali\OneDrive\Desktop\Bootcamp\homework\module3\python-challenge\PyBank\Resources\budget_data.csv"


#reading csv
with open(bank_path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter = ",")
    next(reader)

#saving csv header
    csv_header = next(csvfile)


#variable for the total number of months 
    months = []    

#variable for the total amount of "Profits/Loss" for the entire period
    profit_loss = [] 

#variable for average change in "Profit/Loss" for the entire period
    change_profit_loss = []

    for rows in reader:
        profit_loss.append(int(rows[1]))
        months.append(rows[0])
        
    #calculating the total number of months
    total_months = len(months)
    
    #calculating the total amount of "Profits/Losses" for the entire period
    total_profit_loss = sum(profit_loss)
    
    #calculating average change in "Profits/Losses"
    for x in range(1, len(profit_loss)):
        change_profit_loss.append(((int(profit_loss[x]) - int(profit_loss[x-1]))))
        
    average_change_profit_loss = sum(change_profit_loss)/len(change_profit_loss)
    
    #calculating the greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(change_profit_loss)
    
    #calculating the greatest decrease in profits (date and amount) over the entire period
    greatest_decrease = min(change_profit_loss)
    
    #printing the analysis
    #print the Results
    print("Financial Analysis")

    print("....................................................................................\n")


    print(f"Total months: {total_months}\n")

    print(f"Total: ${total_profit_loss}\n")

    print(f"Average change: ${average_change_profit_loss}\n")

    print(f"Greatest Increase in Profits: {str(months[change_profit_loss.index(max(change_profit_loss))+1])} ${greatest_increase}\n")

    print(f"Greatest Increase in Profits: {str(months[change_profit_loss.index(min(change_profit_loss))+1])} ${greatest_decrease}\n")
    
    
#exporting analysis to txt file 
    file = open("PyBank.txt","w")   

    file.write("Financial Analysis\n")

    file.write("....................................................................................\n")


    file.write(f"Total months: {total_months}\n")

    file.write(f"Total: ${total_profit_loss}\n")

    file.write(f"Average change: ${average_change_profit_loss}\n")

    file.write(f"Greatest Increase in Profits: {str(months[change_profit_loss.index(max(change_profit_loss))+1])} ${greatest_increase}\n")

    file.write(f"Greatest Increase in Profits: {str(months[change_profit_loss.index(min(change_profit_loss))+1])} ${greatest_decrease}\n")
    file.close()