import sys
import os
import re

def main():#also learned how to accept commandline arguments from google
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".py") or not os.path.isfile(sys.argv[1]):
        sys.exit(1)
    else:
        comm = r'\s*#.*$'
        fileP = sys.argv[1]
        lines = 0
        #learned about reading csv files from ai
        with open(fileP, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line:
                        if not re.match(comm, line):
                            lines += 1
        print(lines)
main()



