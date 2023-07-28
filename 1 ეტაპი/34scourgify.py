import csv
import sys
import os

def main():
    if not len(sys.argv) == 3 or not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv") or not os.path.isfile(sys.argv[1]):
        sys.exit(1)
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]

        data = listify(input_file_path)
        create(output_file_path, data)

def listify(file_path):
    data = []
    with open(file_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            data.append(row)
    return data

def create(created_file, collectedData):
    with open(created_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in collectedData:
            if isinstance(row, list):
                if len(row) == 2:
                    lastname_firstname, place = row
                    lastname, firstname = lastname_firstname.split(',')
                    csv_writer.writerow([firstname.strip(), lastname.strip(), place])
                else:
                    csv_writer.writerow(row)

if __name__ == "__main__":
    main()


