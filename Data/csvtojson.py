import os
import csv
import json


def csv_to_json(csv_file_path):
    data = []
    with open(csv_file_path, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    return data

def consolidate_csv_to_json(directory_path):
    consolidated_data = {}

    # Load existing data if dataset.json already exists
    if os.path.isfile('dataset.json'):
        with open('dataset.json', 'r', encoding='utf-8') as json_file:
            consolidated_data = json.load(json_file)

    # Loop through all files in directory
    for filename in os.listdir(directory_path):
        if filename.endswith('.csv') and filename not in consolidated_data:
            csv_file_path = os.path.join(directory_path, filename)
            data = os.path.join(directory_path, filename)
            consolidated_data[filename] = csv_to_json(csv_file_path)

    with open('dataset.json', 'w', encoding='utf-8') as outfile:
        json.dump(consolidated_data, outfile, indent=4)


if __name__ == '__main__':
    dir_path = 'Data'
    consolidate_csv_to_json('Data')