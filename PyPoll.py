# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote. 
import csv
import os

# Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources", "election_results.csv")

# Create filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis
    file_reader = csv.reader(election_data)
    # print each row in the csv file
    header_row = next(file_reader)
    print(header_row)
    # for row in file_reader:
    #     print(row)

# Using the open() function with the "w" mode we will write data to the file
with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")

