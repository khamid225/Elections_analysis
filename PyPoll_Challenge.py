# -*- coding: utf-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Resources/election_results.csv
# Add a variable to load a file from a path.
file_to_load = os.path.join("election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []  # array
county_votes = {}  # dictionary

# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county = ""
largest_turnout = 0

separation = "—" * 25 + "\n"

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:
            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            # Dictionary empty county_votes : {}
            # Syntax county_votes[county_name] = county_votes['Jefferson']
            county_votes[county_name] = 0

            # Dictionary with a kep pair value: {'Jefferson':0}

        # 5: Add a vote to that county's vote count.

        county_votes[county_name] += 1

# This variable will hold all of the output

output = ""

election_results = (
    f"\nElection Results\n"
    "" + separation + ""
    f"Total Votes: {total_votes:,}\n"
    "" + separation + "\n"
    f"County Votes:\n"
)

output += election_results

# 6a: Write a for loop to get the county from the county dictionary.
for county_name in county_votes:
    # 6b: Retrieve the county vote count.
    votes_for_this_county = county_votes[county_name]
    percentage_for_this_county = round(votes_for_this_county / total_votes * 100, 1)

    # 6f: Write an if statement to determine the winning county and get its vote
    # count.
    if votes_for_this_county > largest_turnout:
        largest_county = county_name
        largest_turnout = votes_for_this_county

    # 6d: Print the county results to the terminal.
    output += (f"{county_name}: {percentage_for_this_county}% "
               f"({votes_for_this_county:,})\n")


output += "\n"

# 7: Print the county with the largest turnout to the terminal.
output += (
    "" + separation + ""
    f"Largest County Turnout: {largest_county}\n"
    "" + separation + "\n"
)

for candidate_name in candidate_votes:
    votes = candidate_votes.get(candidate_name)
    percentage_for_this_candidate = round(votes / total_votes * 100, 1)

    output += f"{candidate_name}: {percentage_for_this_candidate}% ({votes:,})\n\n"

    if votes > winning_count:
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = percentage_for_this_candidate

# Print the final vote count (to terminal)

output += (
    "" + separation + ""
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage}%\n"
    "" + separation + ""
)

print(output)

# 6e, 7 and 8
with open(file_to_save, "w") as txt_file:
    txt_file.write(output)
