"""Provide access to knight data
"""
from pprint import pprint

FILE_PATH  = "DATA/knights.txt"

def main():
    """program entry point
    """
    data = read_data()
    pretty_print(data)
    print()
    print_titles(data)
    print()
    print(get_attribute(data, 'Lancelot', 3))

def read_data():
    """Read data from knights file into a dictionary

    :return: dictionary of knight data where key is knight's name
    :rtype: dict
    """
    knights_data = {}

    with open(FILE_PATH) as file_in:
        for raw_line in file_in:
            line = raw_line.rstrip()
            name, title, color, quest, comment = line.split(':')
            knights_data[name] = title, color, quest, comment
    return knights_data

def pretty_print(data):
    """Print the data in human-readable format

    :param data: Dictionary of data
    :type data: dict
    """
    pprint(data)

def print_titles(kdata):
    """Print titles, knights, and quests

    :param kdata: Dictionary of data
    :type kdata: dict
    """
    for name, data in kdata.items():
        print(f"{data[0]:4} {name:10} {data[2]}")
    print()

def get_attribute(data, knight, item):
    """Retrieve one attribute from a knight

    :param data: _description_
    :type data: _type_
    :param knight: _description_
    :type knight: _type_
    :param item: _description_
    :type item: _type_
    :return: _description_
    :rtype: _type_
    """
    return data[knight][item]

main()