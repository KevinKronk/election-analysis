import csv
import os

# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")

# Create filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
total_votes = 0
candidate_votes = {}
winning_candidate = ['', 0, 0]

with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)
    # read the header
    header_row = next(file_reader)
 
    # Loop through csv file rows and calculate total number of votes
    for voting_info in file_reader:
        total_votes += 1
        # If candidate name does not match existing candidates, add them, and then count their votes
        if voting_info[2] not in candidate_votes:
            candidate_votes[voting_info[2]] = 0
        candidate_votes[voting_info[2]] += 1

print(candidate_votes)

# Loop through each candidates votes and calculate the total percentage
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
    # Is the candidates votes greater than the current winning candidates votes 
    if votes > winning_candidate[1]:
        winning_candidate[0:3] = candidate, votes, vote_percentage

# Print the winning candidate
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate[0]}\n"
    f"Winning Vote Count: {winning_candidate[1]:,}\n"
    f"Winning Percentage: {winning_candidate[2]:.1f}%\n"
    f"--------------------------\n")
print(winning_candidate_summary)


# Using the open() function with the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

