import csv
import sys
import os
from tabulate import tabulate

def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".csv") or not os.path.isfile(sys.argv[1]):
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        data = listify(file_path)
        print(tabulate(data, headers='firstrow', tablefmt='grid'))


def listify(file_path):
    data_list = []
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data_list.append(row)
    return data_list


main()