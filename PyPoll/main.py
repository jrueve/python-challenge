#import necessary systems
import os, csv

#select correct csv from resource file
csvpath = os.path.join("Resources","election_data.csv")

#open csv read through each line and define the list or variables needed
with open(csvpath, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    totalvotes = 0
    candidatelist = []
    votelist = []
    votecount = {}

#loop through each row in csv to count votes cast, define candidates as correct collumn
    for row in csvreader:
        totalvotes += 1
        candidate = row[2]
        votelist.append(candidate)
        #if candidate not already on list then add to list when name changes
        if candidate not in candidatelist:
            candidatelist.append(candidate)
            #change candidates count to zero to loop through next person at zero
            votecount[candidate] = 0
            #add 1 vote per every time candidate is named in row
        votecount[candidate] = votecount[candidate] + 1
        #find votes specifically for one candidate and then find the percent of the total vote the candidate one
    for vote in votecount:
        count = votecount[vote]
        countpercent = (count/totalvotes) *100
        #print vote percent for candidate
        print(f"vote percent {countpercent} : candidate name {vote}")
    #winning candidate finder
    winner = max(votecount.values())
    winpercent = round((winner/totalvotes)*100,2)
    win = [key for key in votecount if votecount[key] == winner]
    #print(str(win))

    #print candidate list
    print(candidatelist)
    #print total votes cast
    print(totalvotes)
    #print vote per person
    print(votecount)

with open(output_file, "w") as outputfile:
    print("Election Results",file=outputfile)
    print("---------------------------------",file=outputfile)
    print(f"Total Votes : {totalvotes }",file=outputfile)
    print("---------------------------------",file=outputfile)
    print(f'Charles Casper Stockham : {countpercent}% ({candidatelist["Charles Casper Stockham"]})',file=outputfile)
    print(f'Diana DeGette : {countpercent}% ({candidatelist["Diana DeGette"]})',file=outputfile)
    print(f'Raymon Anthony Doane : {countpercent}% ({candidatelist["Raymon Anthony Doane"]})',file=outputfile)
    print("---------------------------------",file=outputfile)
    print(f'Winner :  {winner}',file=outputfile)
    print("---------------------------------",file=outputfile)
