"""
Read and output knights and their titles
"""
from pprint import pprint

FILE_PATH = "DATA/knights.txt"

def main():
    "Program starting point."
    knight_data = read_file()  # read in the data
    show_data(knight_data)
    print(f"{get_title('Arthur', knight_data) = }")
    print(f"{get_title('Lancelot', knight_data) = }")

def read_file():
    """
        Read all data into a dictionary.

        Returns dictionary of name:title pairs
    """
    titles = {}  # dict of name/title pairs

    with open(FILE_PATH) as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()
            name, title, _, _, _ = line.split(':')
            titles[name] = title  # create dict element
    return titles

def show_data(data):
    """
    Pretty-print the name/title data
    """
    pprint(data)

def get_title(knight_name, data):
    """
    Retrieve the title for a specified knight
    """
    return data[knight_name]


main()