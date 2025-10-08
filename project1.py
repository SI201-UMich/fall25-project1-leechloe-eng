# Name: Chloe Lee
# Student ID: 1488 4654
# Email: leechloe@umich.edu
# Collaborators: Zachary Landau and Norah Smith
# AI tools used: ChatGPT for guidance on code structure
# Functions created: read_csv, calc_average_yield_per_crop, calc_highest_yield_crop_per_region, calc_average_temp_per_region, calc_total_area_harvested_by_year, calc_average_rainfall_per_region, calc_average_fertilizer_per_crop

import csv

def read_csv(filename):
    data = []
    with open(filename, 'r', encoding= 'utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def calc_average_yield_per_crop(data):
    totals = {}
    counts = {}
    for row in data:
        crop = row['Crop']
        try:
            yield_value = float(row['Yield_tons_per_hectare'])
        except:
            continue
        totals[crop] = totals.get(crop, 0) + yield_value
        counts[crop] = counts.get(crop, 0) + 1

    averages = {}
    for crop in totals:
        averages[crop] = totals[crop] / counts[crop]
    return averages

def calc_highest_yield_crop_per_region(data):
    highest = {}
    for row in data:
        region = row['Region']
        crop = row['Crop']
        try:
            yield_value = float(row['Yield_tons_per_hectare'])
        except:
            continue
        if region not in highest or yield_value > highest[region][1]:
            highest[region] = (crop, yield_value)

    result ={}
    for country in highest:
        result[country] = highest[country][0]
    return result

def calc_average_temp_per_region(data):
    totals = {}
    counts = {}
    for row in data:
        region = row['Region']
        try:
            temp_value = float(row['Avg_temp'])
        except:
            continue
        totals[region] = totals.get(region, 0.0) + temp_value
        counts[region] = counts.get(region, 0) + 1

def calc_total_area_harvested_by_year(data):
    totals = {}
    area_col = 'Area_harvested'
    for row in data:
        year = row['Year']
        try:
            area_value = float(row.get(area_col, ''))
        except:
            continue
        totals[year] = totals.get(year, 0.0) + area_value
    return totals

def calc_average_rainfall_per_region(data):
    totals = {}
    counts = {}
    rain_col = 'Rainfall_mm'
    for row in data:
        region = row['Region']
        try:
            rainfall_value = float(row.get(rain_col, ''))
        except:
            continue
        totals[region] = totals.get(region, 0.0) + rainfall_value
        counts[region] = counts.get(region, 0) + 1
    
    averages = {}
    for region in totals:
        averages[region] = totals[region] / counts[region]
    return averages

def calc_average_fertilizer_per_crop(data):
    totals = {}
    counts = {}
    fert_col = 'Fertilizer_Used'
    for row in data:
        crop = row['Crop']
        try:
            fertilizer_value = float(row.get(fert_col, ''))
        except:
            continue
        totals[crop] = totals.get(crop, 0.0) + fertilizer_value
        counts[crop] = counts.get(crop, 0) + 1
    
    averages = {}
    for crop in totals:
        averages[crop] = totals[crop] / counts[crop]
    return averages

if __name__ == "__main__":
    pass