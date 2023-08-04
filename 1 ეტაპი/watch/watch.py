import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        link = s.split('"')[1]

        regex = r"(?:https?:)?//(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"

        answer = bool(re.match(regex, link))

        if answer == True:

            link = link.split("/")
            length = len(link)
            id = link[length-1]
            returnable = f'https://youtu.be/{id}'
            return returnable

        else:
            pass

    except IndexError:

        pass


if __name__ == "__main__":
    main()