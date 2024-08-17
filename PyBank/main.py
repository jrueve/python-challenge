#import  necessary systems
import os
import csv
import pathlib

#select correct csv from resource file
csvpath = os.path.join("Resources","budget_data.csv")

#define variables
datelist = []
monthlydiff = []
avgChange = 0

#open csv read through each line and define the list or variables needed
with open(csvpath, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    data_dict = {}
    totalmonths = 0
    total = 0
    datelist = []
    profitlist = []

#loop through each row in csv to count total months profit, collect dates and profit in correct collumn
    for row in csvreader:
        #increase month count every row
        totalmonths += 1
        #count profit total every row
        total = total + int(row[1])
        #define date column
        date = row[0]
        #define profit column
        profit = row[1]
        #if date not already on list then add to list when name changes
        if date not in datelist:
            datelist.append(date)
        #if profit not already on list then add to list when name changes
        if profit not in profitlist:
            profitlist.append(profit)
        #create dictionary from two lists of date and profit to read instaed of csv when needed later
    dict = {datelist[i]: profitlist[i] for i in range(len(datelist))}
    #collect first value profit in list
    beginprofit = list(dict.values())[0]
    #define final profit as zero to start
    finalprofit = 0

    for i in range(0, len(profitlist)):
        profitlist[i] = int(profitlist[i])
    
    #define average change as zero to start 
    avgChange = 0
    #loop through number of values in profitlist
    for i in range(0, len(profitlist)):
        #calculate differeence of beginning value and final value 
        diff = int(finalprofit) - int(beginprofit)
        #add to list
        monthlydiff.append(diff)
        #chnage beginning profit
        beginprofit = profitlist[i -1]
        #chnage final profit
        finalprofit = profitlist[i]
    #calculate the average change
    avgChange = round(sum(monthlydiff)/len(monthlydiff),2)

    #calculate max monthly change
    greatestincrease = max(monthlydiff)
    #calculate min monthly change
    greatestdecrease = min(monthlydiff)
    #get index value for max change
    greatest_increase_index = monthlydiff.index(greatestincrease)
    #get index value for min change
    greatest_decrease_index = monthlydiff.index(greatestdecrease)
    #use index value to find month greatest increase happened
    greatestincreasedate = datelist[greatest_increase_index -1]
    #use index value to find month greatest decrease happened
    greatestdecreasedate = datelist[greatest_decrease_index-1]

#print our findings
file_path = pathlib.Path("output_file.txt")
with file_path.open( "w") as outputfile:
    print("Financial Ananlysis",file=outputfile) 
    print("--------------------------------",file =outputfile)
    print("Total Months :",totalmonths,file =outputfile)  
    print(f"Total : ${total}",file =outputfile)
    print(f"Average Change : ${avgChange}",file =outputfile)
    print(f"The Greatest Increase in Profits : { greatestincreasedate} (${greatestincrease})",file =outputfile)
    print(f"The Greatest Decrease in Profits : { greatestdecreasedate} (${greatestdecrease})",file =outputfile)