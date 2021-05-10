# Elections_analysis
Written Analysis of the Election Audit 

The purpose of this election audit is to calculate the total amount of votes, to calculate the votes count by county and by candidate. Also, to find out which candidate has the highest amount of votes.

369,711 total votes were cast in this election.

The county votes were the following: 
Jefferson: 10.5% (38,855)
Denver: 82.8% (306,055)
Arapahoe: 6.7% (24,801)

Denver had the largest number of votes.

Charles Casper Stockham: 23.0% (85,213)
Diana DeGette: 73.8% (272,892)
Raymon Anthony Doane: 3.1% (11,606)

Diana DeGette won the election with a vote count of 272,892 which is 73.8% of elections.

This script can be used for any election analysis in the future for any analyzations or calculations.
2 scrips that can be modified are: 
The first script is to Add a variable to load a file from a path. Instead of "election_results.csv", you'd modify this by entering your file name from your path.
file_to_load = os.path.join("../", "election_results.csv") 
The second script is to Calculate the percentage of votes for the county.
The script is vote_percentage = float(county_vote) / float(total_votes) * 100
        #    county_votes = (
        #    f"{county_name}: {vote_percentage:.1f}% ({county_vote:,})\n")
Instead of "county_vote" in the float, you can enter whatever you named your dictionary.
