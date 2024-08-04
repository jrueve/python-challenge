import os, csv

csvpath = os.path.join("Resources","election_data.csv")

candidatelist = []
totalvotes = 0

with open(csvpath, newline="", encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    vote0 = 0
    vote1 = 0
    vote2 = 0
    totalvotes = 0
    candidatelist = []
    votelist = []

    for row in csvreader:
        totalvotes += 1
        candidate = row[2]
        votelist.append(candidate)
        if candidate not in candidatelist:
            candidatelist.append(candidate)
    candidatecount = len(candidatelist)

    print(candidatelist)
    print(totalvotes)
    print(candidatecount)

    candidates = list()
    for i in votelist:
        name == candidatelist[i]
        candidates.append(votelist.count(name))


''' votes = 0
    for index in votelist:
        if votelist[index] != votelist[index+1]:
            print(votes)
            votes = 0
        elif votelist[index] == votelist[index+1]:
            votes += 1'''