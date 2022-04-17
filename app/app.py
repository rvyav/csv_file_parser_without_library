import operator
import os

from pprint import pprint
from typing import Dict, List


# folder that contain
# the csv file data to work with
csv_folder = os.getcwd() + "/app/data/"


def handler() -> List[Dict[str, str]]:
    """
    The function accept an input in CSV file
    """
    files = [file for file in os.listdir(csv_folder) if file.endswith(".csv")]

    if not files:
        return "No CSV file found in the data directory"

    files_range = [*range(1, len(files) + 1)]

    # create a selection of CSV files only
    # to choose from based on what is found
    selection = dict(zip(files_range, files))

    # make sure `files` array is not empty
    while files:
        print("Current file(s) found: {}".format(selection))
        print("Your current KEY choice(s): {}".format(list(selection.keys())))
        
        try:
            user_input = int(input("Select a KEY to process the file, select a NUMBER from choice(s): "))
        except:
            continue
        
        if isinstance(user_input, int):
            if user_input in selection.keys():
                for key, value in selection.items():
                    if user_input == key:
                        result = parse_file(csv_folder + value)
                        return result
                break
        else:
            continue

        _clean_terminal()
        print("Wrong value, try again \n")


def parse_file(csv_file: str) -> List[Dict[str, str]]:
    with open(csv_file, encoding="utf-8") as file:
        results = []
        
        for values in file:
            if values.endswith("\n"):
                value = values.rstrip("\n")
            words = value.split(",")
            
            results.append((words))

        headers = _remove_trailing_space(results[0])
        content = results[1:]

        # create a readable list of dictionnaries
        # made of columns names and their corresponding
        # values for each row
        data = [dict(zip(headers, value)) for value in content]

        while data:
            user_column_input = input("Select a Column to sort: {}\n".format(headers))

            if user_column_input in headers:
                # sort column in descending string order
                data.sort(key=operator.itemgetter(user_column_input), reverse=True)
                return data

            _clean_terminal()
            print("Wrong value, try again \n")


# PEP-8, the Python Style Guide for helper functions
# https://peps.python.org/pep-0008/#naming-conventions
def _clean_terminal():
    return os.system("clear")


def _remove_trailing_space(arr: List[str]) -> List[str]:
    """Make sure the string have no trailing spaces."""
    return [value.strip(" ") for value in arr]


if __name__ == "__main__":
    result = handler()
    # human readable result output
    pprint(result)
