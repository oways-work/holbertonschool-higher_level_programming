#!/usr/bin/python3
"""
Module to convert CSV data to JSON format using serialization.
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Reads a CSV file and writes the data to data.json in JSON format.

    Args:
        csv_filename (str): The name of the input CSV file.

    Returns:
        bool: True if the conversion was successful, False if the file was not found.
    """
    try:
        # Read the CSV file and convert rows to dictionaries
        with open(csv_filename, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            # Convert the iterator to a list of dictionaries
            data = list(csv_reader)

        # Serialize the list of dictionaries to JSON and write to file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
