import os, csv

csvpath = os.path.join("Resources","budget_data.csv")

total = 0
date = []
profit = []

with open(csvpath, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    totalmonths = 0  
    datalist = list(csvreader)
    for row in csvreader: 
        totalmonths += 1

        total = total + int(row[1])
        date.append(row[0])
        profit.append(int(row[1]))
    
    beginprofit = int(datalist[0][1])
    finalprofit =  0
    diff = 0
    monthlydiff = []

    for i in range(1, len(datalist)):
        finalprofit = int(datalist[i][1])
        diff = finalprofit - beginprofit
        monthlydiff.append(diff)
        beginprofit = int(datalist[i][1])
    avgChange = round(sum(monthlydiff)/len(monthlydiff),2)
    greatestincrease = max(monthlydiff)
    greatestdecrease = min(monthlydiff)
    greatestincreasedate = date[greatestincrease]
    greatestdecreasedate = date[greatestdecrease]



    print(totalmonths)
    print(total)
    print(beginprofit)
    print(avgChange)
    print(greatestincrease)
    print(greatestdecrease)