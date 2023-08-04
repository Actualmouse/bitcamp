import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    regex = r"\bum\b"
    amount = len(re.findall(regex, s.lower()))
    return amount


if __name__ == "__main__":
    main()