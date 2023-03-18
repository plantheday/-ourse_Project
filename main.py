from utils import get_data, get_filtered_data, get_formatted_data, get_last_data

import json


def main():
    with open('operations.json', 'r', encoding='utf-8') as file:
        operations = json.load(file)
    COUNT_LAST_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data = get_data(operations)
    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_data(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    for row in data:
        print(row)


if __name__ == "__main__":
    main()
