#import necessary systems
import os, csv, pathlib

#select correct csv from resource file
csvpath = os.path.join("Resources","election_data.csv")

#open csv read through each line and define the list or variables needed
with open(csvpath, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

#define empty variables to be filled later
    totalvotes = 0
    candidatelist = []
    votelist = []
    votecount = {}

#loop through each row in csv to count votes cast, define candidates as correct collumn
    for row in csvreader:
        #count each row to get total votes
        totalvotes += 1
        #define candidate row
        candidate = row[2]
        #add every name in row to list to be counted and referred to later
        votelist.append(candidate)
        #if candidate not already on list then add to list when name changes
        if candidate not in candidatelist:
            candidatelist.append(candidate)
            #change candidates count to zero to loop through next person at zero
            votecount[candidate] = 0
            #add 1 vote per every time candidate is named in row
        votecount[candidate] = votecount[candidate] + 1

    #create list of percentages for each candidate to be stored in
    percentlist = []
    #loop through votes for each candidate in votecount
    for vote in votecount:
        #make count equal to value of key, which is candidate name in votecount 
        count = votecount[vote]
        #get percent votes for each candidate based on number of votes divided by total votes and multiplied by 100 for percent
        countpercent = (count/totalvotes) *100
        #add percentages to list to reference later
        percentlist.append(countpercent)

        #print vote percent for candidate
        print(f"vote percent {round(countpercent,3)} : candidate name {vote}")

    #winning candidate finding number of votes
    winner = max(votecount.values())
    #round the percent
    winpercent = round((winner/totalvotes)*100,3)
    #find name of winner
    win = [key for key in votecount if votecount[key] == winner]
    #print(str(win))

    #print candidate list
    print(candidatelist)
    #print total votes cast
    print(totalvotes)
    #print vote per person
    print(votecount)

#print to text file all our results in string
file_path = pathlib.Path("Analysis","output_file.txt")
with file_path.open( "w") as outputfile:
    print("Election Results",file=outputfile)
    print("---------------------------------",file=outputfile)
    print(f"Total Votes : {totalvotes }",file=outputfile)
    print("---------------------------------",file=outputfile)
    print(f'Charles Casper Stockham : {round(percentlist[0],3)}% ({votecount.get("Charles Casper Stockham")})',file=outputfile)
    print(f'Diana DeGette : {round(percentlist[1],3)}% ({votecount.get("Diana DeGette")})',file=outputfile)
    print(f'Raymon Anthony Doane : {round(percentlist[2],3)}% ({votecount.get("Raymon Anthony Doane")})',file=outputfile)
    print("---------------------------------",file=outputfile)
    print(f'Winner :   {str(win)}',file=outputfile)
    print("---------------------------------",file=outputfile)
