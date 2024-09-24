# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:29:29 2024

@author: ibraa
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

import csv
import os

file_to_load = os.path.join("Resources", "C:/Users/ibraa/OneDrive/Desktop/VU-VIRT-DATA-PT-08-2024-U-LOLC/challange 3-20240923T231915Z-001/challange 3/Starter_Code/PyPoll/Resources/election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "C:/Users/ibraa/OneDrive/Desktop/VU-VIRT-DATA-PT-08-2024-U-LOLC/challange 3-20240923T231915Z-001/challange 3/Starter_Code/PyPoll/Resources/election-data.txt")  # Output file path

total_votes = 0
candidates = {}
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    header = next(reader)
    for row in reader:
        print(". ", end="")
        total_votes += 1
        candidate_name = row[2]
        if candidate_name not in candidates:
            candidates[candidate_name] = 0 

        candidates[candidate_name] += 1

with open(file_to_output, "w") as txt_file:
    print(f"Total Votes: {total_votes}")
    txt_file.write(f"Total Votes: {total_votes}\n")

    winning_candidate = ""
    winning_count = 0
    for candidate, votes in candidates.items():

        vote_percentage = (votes / total_votes) * 100
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        candidate_results = f"{candidate}: {vote_percentage:.3f}% ({votes})"
        print(candidate_results)
        txt_file.write(candidate_results + "\n")
    winning_summary = (
        f"\nWinning Candidate: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {(winning_count / total_votes) * 100:.3f}%\n"
    )
    print(winning_summary)
    txt_file.write(winning_summary)