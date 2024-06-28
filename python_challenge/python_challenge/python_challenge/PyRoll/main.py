
import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

ballot_id = []
county = []
candidates = []


print("Election Results")
print("----------------------------")


with open(election_data,newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")
    csvheader = next(csvreader)

    for row in csvreader:
        ballot_id.append(int(row[0]))
        county.append(row[1])
        candidates.append(row[2])

    votes_total = len(ballot_id)
    print(f"Total Votes:", votes_total)

    print("----------------------------")

    #A complete list of candidates who received votes
    #The percentage of votes each candidate won
    #The total number of votes each candidate won

    candidates_list = list(set(candidates))
    
    for all_candidates in candidates_list:
        candidates_votes = candidates.count(all_candidates)
        candidates_percentage = (candidates_votes / votes_total) * 100
        print(f"{all_candidates}: {candidates_percentage:.3f}% ({candidates_votes})")
  
    print("----------------------------")
    print(f"Winner: {max(set(candidates), key = candidates.count)}")
    print("----------------------------")

    #Export a text file with the results
    with open("text_file2.txt", "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------------\n")
        file.write(f"Total Votes: {votes_total}\n")
        file.write("-------------------------------\n")
        file.write(f"{all_candidates}: {candidates_percentage:.3f}% ({candidates_votes})\n")
        file.write("-------------------------------\n")
        file.write(f"Winner {max(set(candidates), key = candidates.count)}\n")
        file.write("-------------------------------\n")
        

