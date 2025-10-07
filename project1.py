# Name: Chloe Lee
# Student ID: 1488 4654
# Email: leechloe@umich.edu
# Collaborators: Zachary Landau and Norah Smith
# AI tools used: ChatGPT for guidance on code structure
# Functions created: read_csv, calc_average_yield_per_crop

import csv

def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def calc_average_yield_per_crop(data):
    totals = {}
    counts = {}
    for row in data:
        crop = row['Crop']
        yield_value = float(row['Yield_hg_per_ha'])
        totals[crop] = totals.get(crop, 0) + yield_value
        counts[crop] = counts.get(crop, 0) + 1
    averages = {}
    for crop in totals:
        averages[crop] = totals[crop] / counts[crop]
    return averages

def calc_highest_yield_crop_per_country(data):
    highest = {}
    for row in data:
        country = row['Country']
        crop = row['Crop']
        yield_value = float(row['Yield_hg_per_ha'])
        if country not in highest or yield_value > highest[country][1]:
            highest[country] = (crop, yield_value)
    result ={}
    for country in highest:
        result[country] = highest[country][0]
    return result