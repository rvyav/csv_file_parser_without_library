import os

from pprint import pprint
from typing import Dict, List


# the folder that contain the CSV
# files to work with
csv_folder = os.getcwd() + "/data/"


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
                        return value
                break
        else:
            continue

        _clean_terminal()
        print("Wrong value, try again \n")


# PEP-8, the Python Style Guide for helper functions
# https://peps.python.org/pep-0008/#naming-conventions
def _clean_terminal():
    return os.system("clear")


if __name__ == "__main__":
    result = handler()
    # humand readable result output
    pprint(result)
