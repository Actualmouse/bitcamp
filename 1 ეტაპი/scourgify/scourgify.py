import sys
import os
import csv

def main():
    if len(sys.argv) != 3 or not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv") or not os.path.isfile(sys.argv[1]):
        sys.exit(1)

    inputfl = sys.argv[1]
    outptfl = sys.argv[2]

    try:
        with open(inputfl, 'r') as inp, open(outptfl, 'w', newline='') as outp:
            rdr = csv.reader(inp, quotechar='"')

            writer = csv.writer(outp)

            header = next(rdr)


            writer.writerow(['first', 'last', 'house'])

            for row in rdr:
                name, house = row
                first_name, last_name = name.split(', ', 1)
                writer.writerow([last_name, first_name, house])


    except Exception as e:
        sys.exit(f"ERR0R: {e}")

if __name__ == "__main__":
    main()


#python scourgify.py before.csv after.csv

#check50 cs50/problems/2022/python/scourgify
#submit50 cs50/problems/2022/python/scourgify