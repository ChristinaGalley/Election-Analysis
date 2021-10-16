# Election-Analysis

## Project Overview
A Colorado Board of Elections employee had given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code, 1.60.2

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the elction.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Overview of Election Audit
The purpose of this election audit analysis is to determine the voter turnout for each county, the percentage of votes from each county out of the total count, and the county with the highest turnout.

## Election-Audit Results
- **369,711** votes were cast in this congressional election.
- The number of votes for each county in the precinct is determined using the code: `votes = county_votes[county_name]`. The percentage of total votes for each county in the precinct is determined using the code: `vote_percentage = float(votes) / float(total_votes) * 100`.
- **Denver** county had the largest number of votes.
- The number of votes each candidate received is determined using the code: `votes = candidate_votes.get(candidate_name)`. The percentage of the total votes each candidate received is determined using the code: `vote_percentage = float(votes) / float(total_votes) * 100`.
- **Diana DeGette** won the election. Her vote count is **272,892**, and the percentage of the total votes is **73.8%**.
- These results are printed on the election_analysis.txt file as shown in the image below: ![picture alt](https://github.com/ChristinaGalley/Election-Analysis/blob/main/Analysis/Election_Analysis_results_txtpage_%20image.png)

## Election-Audit Summary
Although this script was used to for an election-audit of the recent local congressional election, it can be used—with some modifications—for any election. To modify the script for a differnt election, add a variable to load the corresponding results file from a path by modifying this code: `file_to_load = os.path.join("Resources", "election_results.csv")` to use the appropriate folder and file. Make sure the results file is formated in same way with 3 columns indicating, Ballot ID, County, and Candidate. Otherwise further modifcitions will be necessary, for example when getting candidate name from each row using code: `candidate_name = row[2]` the column number containing candidate names may not be listed under 2 if the format is different. 
