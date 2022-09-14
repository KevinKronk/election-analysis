# Election Analysis with Python

## Overview of Election Audit

### Purpose
The Colorado Board of Elections need Seth and Tom to submit an election audit on the most recent local congressional election. They initially needed info on the total number of votes, the votes per candidate, the percentage of the total votes for each candidate, and who the winning candidate was. The election commission then requested some additional data on the counties participating in the election. They need the voter turnout in each county, the percentage of total votes for each county, and the county with the highest voter turnout. 

### Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code. 1.71.0

## Election Audit Results 
  - In total, 369,711 votes were cast in this congressional election.
  - County Results:
    - Jefferson county received 38,855 votes which made up 10.5% of the total votes. 
    - Denver county received 306,055 votes for 82.8% of the total. 
    - Arapahoe county received 24,801 votes for 6.7% of the total. 
  - Therefore, Denver county had the largest number of votes. 
  - Candidate Results:
    - Charles Casper Stockham received 85,213 votes which made up 23.0% of the total votes. 
    - Diana DeGette received 272,892 votes for 73.8% of the total. 
    - Raymon Anthony Doane received 11,606 votes for 3.1% of the total. 
  - Therefore, Diana DeGette won the election with 272,892 votes and 73.8% of the total. 
  
![Election Results](Resources/Election_Results_Command_Line.png)

## Election Audit Summary
This script can be used for any election in which the winner is chosen by plurality (getting more votes than everyone else) rather than majority (winning more than half the votes). If we wanted to use this script in a majority election, like for the Presidential election, we would first need to change all the county variables, lists, and dictionaries to the appropriate name, in this case state. So assuming the data contained the Ballot ID, State, and Candidate, we would have state_options, state_votes, largest_state, largest_state_votes, state_vote, state_percentage, and state_results. This would also include changes to the command line print statements and the write statements to our election_results.txt file. The part of the code in which we determine which state had the largest voter turnout could remain the same, as we only need the one that had more than any other. For the part of the code where we determine which candidate won, we would loop through all the candidates and if one has greater than 50% of the vote (or technically greater than or equal to 270 electoral college votes), then they are saved as the winning candidate. This would work because only one candidate can have more than half the votes. Outside the loop, another if statement could be used to print the winning candidate, with the else statement being used to print that there is no clear winner in the case that no candidate gets over 50% of the vote. The only other change that might be useful would be to sort the states and candidates in alphabetical order, so they're easier to read. 
