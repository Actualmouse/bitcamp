import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        regex = r':'
        s = s.split(" ")
        if not len(s) == 5 or not s[2] == "to":
            raise ValueError

        first = s[0]
        second = s[3]

        firstDef = s[1]
        secondDef = s[4]

        if not first.isdigit() and bool(re.search(regex, first)) == False:
            raise ValueError
        else:
            firstHrs = first
            firstMins = "00"

        if not second.isdigit() and bool(re.search(regex, second)) == False:
            raise ValueError
        else:
            secondHrs = second
            secondMins = "00"

        if bool(re.search(regex, first)) == True:
            first = first.split(":")
            firstHrs = first[0]
            firstMins = first[1]
            if int(firstHrs) >= 0 and int(firstHrs) <= 12:

                pass
            else:
                raise ValueError
            if int(firstMins) >= 0 and int(firstMins) <= 60:

                pass
            else:
                raise ValueError

        if bool(re.search(regex, second)) == True:
            second = second.split(":")
            secondHrs = second[0]
            secondMins = second[1]
            if int(secondHrs) >= 0 and int(secondHrs) <= 12:
                pass
            else:
                raise ValueError
            if int(secondMins) >= 0 and int(secondMins) < 60:
                pass
            else:
                raise ValueError


        #return firstHrs,firstMins,secondHrs,secondMins

        if firstDef.upper() == "AM":
            firstHrs = firstHrs
        elif firstDef.upper() == "PM" and not int(firstHrs) == 12:
            firstHrs = 12+int(firstHrs)

        if secondDef.upper() == "AM":
            secondHrs = secondHrs
        elif secondDef.upper() == "PM" and not int(secondHrs) == 12:
            secondHrs = 12+int(secondHrs)


        if len(str(secondMins)) == 1:
            raise ValueError
        if len(str(secondHrs)) == 1:
            secondHrs = f"0{secondHrs}"
        if len(str(firstMins)) == 1:
            raise ValueError
        if len(str(firstHrs)) == 1:
            firstHrs = f"0{firstHrs}"


        if firstDef.upper() == "AM" and int(firstHrs) == 12:
            firstHrs = "00"
        elif firstDef.upper() == "PM" and int(firstHrs) == 12:
            firstHrs = "12"

        if secondDef.upper() == "AM" and int(secondHrs) == 12:
            secondHrs = "00"
        elif secondDef.upper() == "PM" and int(secondHrs) == 12:
            secondHrs = "12"


        finalValue = f"{firstHrs}:{firstMins} to {secondHrs}:{secondMins}"

        return finalValue


    except ValueError or IndexError:
        sys.exit("ValueError")



if __name__ == "__main__":
    main()