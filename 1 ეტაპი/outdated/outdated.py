import re

monthsDict = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

#MM/DD/YYYY > YYYY-MM-DD
#MM DD, YYYY > YYYY-MM-DD
#else main()

def main():
    userInput = checkValues(input("Date: "))

def checkValues(date):

    firstPtrn = r"^[a-zA-Z]+ \d{1,2}, \d{4}$"
    secondPtrn = r"^\d{1,2}/\d{1,2}/\d{4}$"

    if date.count(",") == 1 and date.count("/") == 0 and bool(re.match(firstPtrn, date)):
        dateArr = date.split(",")
        if dateArr[0].split(" ")[0] in monthsDict.keys():
            inputMonth = dateArr[0].split(" ")[0]
            dayNum = dateArr[0].split(" ")[1]
            monthNum = monthsDict[inputMonth]
            yearNum = date.split(" ")[2]

            if int(monthNum) <= 12 and int(dayNum) <= 31:
                reform(monthNum, dayNum, yearNum)
            else:
                main()
        else:
            main()
    date = date.replace(" ","")
    if date.count("/") == 2 and date.count(",") == 0 and bool(re.match(secondPtrn, date)):
        dateArr = date.split("/")
        monthNum = dateArr[0]
        dayNum = dateArr[1]
        yearNum = dateArr[2]

        if int(monthNum) <= 12 and int(dayNum) <= 31:
            reform(monthNum, dayNum, yearNum)
        else:
            main()
    else:
        main()

def reform(MM, DD, YYYY):
    if len(str(MM)) == 1:
        MM = f"0{MM}"
    if len(str(DD)) == 1:
        DD = f"0{DD}"

    print(f"{YYYY}-{MM}-{DD}")
    exit()

main()