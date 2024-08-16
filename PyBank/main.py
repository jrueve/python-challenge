#import  necessary systems
import os
import csv

#select correct csv from resource file
csvpath = os.path.join("Resources","budget_data.csv")

#define variables
total = 0
datelist = []
profit = []

#open csv read through each line and define the list or variables needed
with open(csvpath, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#loop through each row in csv to count months, count the total for the financial analysis
    totalmonths = len(datalist)
    for row in csvreader:  
        total = total + int(row[1])
        #get date for each row
        datelist.append(row[0])
        #get profit number of each row
        profit.append(int(row[1]))
        print(row[0])
        #define profit start value
    beginprofit = int(datalist[0][1])
    #set final profit value to 0
    finalprofit =  0
    diff = 0
    monthlydiff = []
    print(datelist)
    #print(datelist)

#loop through copy of csvreader 
    for i in range(1, len(datalist)):
        #get final profit from list
        finalprofit = int(datalist[i][1])
        #check the difference from the final to begininng profit of month
        diff = finalprofit - beginprofit
        #add to list
        monthlydiff.append(diff)
        #change beginning profit to be used for next month value
        beginprofit = int(datalist[i][1])
        #find average of monthly difference
    avgChange = round(sum(monthlydiff)/len(monthlydiff),2)
    #find greatest increase and decrease seen betwwen months of profit
    greatestincrease = max(monthlydiff)
    greatestdecrease = min(monthlydiff)
    #find date the greatest increase and decrease of profit took place
    greatestincreasedate = max(datelist)
    greatestdecreasedate = min(datelist)

#print our findings
    print(totalmonths)
    print(total)
    print(beginprofit)
    print(avgChange)
    print(greatestincrease)
    print(greatestdecrease)
    print(greatestincreasedate)
    print(greatestdecreasedate)