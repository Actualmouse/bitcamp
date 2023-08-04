from datetime import date
from datetime import datetime
from datetime import timedelta
import inflect
import sys


#yyyy-mm-dd
def main():
    userInput = check(input('Date of Birth: '))
    print(userInput)

def check(userInput):
    try:
        inf = inflect.engine()

        today = str(date.today())

        datetime.strptime(userInput, "%Y-%m-%d")

        birthY = int(userInput.split("-")[0])
        birthM = int(userInput.split("-")[1])
        birthD = int(userInput.split("-")[2])

        todayDate = date.today()
        birthDate = date(birthY,birthM,birthD)

        differential = todayDate - birthDate
        minutes = differential.days * 1440

        val = f'{inf.number_to_words(minutes).capitalize().replace("and ","")} minutes'
        return val

    except ValueError:
        sys.exit("Invalid")


if __name__ == "__main__":
    main()