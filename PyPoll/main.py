
#importing files for program
import os
import csv

#reading csv file
pollData = os.path.join(".","Resources","election_data.csv")

with open(pollData, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

  # calculating total number of votes cast
    next(csvreader)
    data = list(csvreader)
    row_count = len(data)

  # calculating the unique candidates 
    candidates = []
    name_candidate = []
    for i in range (0,row_count):
        candidate = data[i][2]
        name_candidate.append(candidate)
        if candidate not in candidates: 
            candidates.append(candidate)
    num_of_candidates = len(candidates)

  # The total number of votes each candidate won and the percentage of votes per candidate
    votes = []
    percentage = []
    for j in range (0,num_of_candidates):
        name = candidates[j]
        votes.append(name_candidate.count(name))
        vote_percent = votes[j]/row_count
        percentage.append(vote_percent)

  # calculating the winner of the election based on number of votes
    winner = votes.index(max(votes))    

  # Print the election result analysis 
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {row_count:,}")
    print("----------------------------")
    for k in range (0,num_of_candidates): 
        print(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    print("----------------------------")
    print(f"Winner: {candidates[winner]}")
    print("----------------------------")

  #exporting analysis to txt file 
    file = open("PyPoll.txt","w")   

    file.write("Election Results \n")

    file.write("....................................................................................\n")


    file.write(f"Total votes: {row_count}\n")
    for k in range (0,num_of_candidates): 
      file.write(f"{candidates[k]}: {percentage[k]:.3%} ({votes[k]:,})\n")
    
    file.write("...................................................................................\n")
        
    file.write(f"Winner: {candidates[winner]}")
  
    file.close()

    