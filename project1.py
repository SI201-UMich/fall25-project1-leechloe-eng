# Name: Chloe Lee
# Student ID: 1488 4654
# Email: leechloe@umich.edu
# Collaborators: Zachary Landau and Norah Smith
# AI tools used: ChatGPT for guidance on code structure
# Functions created: read_csv

import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data