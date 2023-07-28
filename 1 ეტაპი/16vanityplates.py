import re

def main():

    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    letters_pattern = r"^[a-zA-Z]+$"

    if bool(re.match(letters_pattern, s)) and not any(char for char in s if char.isalnum() == False) and 2 <= len(s) <= 6:
        return True
  

    i=-1
    letters = r"[^a-zA-Z]"
    pattern = r"[^a-zA-Z0-9]"
    nums = r"\d"
    myArr = []   
    TorF = 0
    
    if len(s) == 1:
        print("Invalid")
        exit()

    for char in s:
        i = i+1
        myArr.append(char)

    if myArr[0].isalpha() and myArr[1].isalpha():
        TorF += 1    


    length = len(myArr)

    strLen = len(s)
    checkNum = 1
    checkOne = 1

    if length >= 2 and 6 >= length:
        TorF += 1
    
    if bool(re.search(nums, s)):
        checkOne = 2
        if s[length-1].isdigit() and s[length-2].isdigit():
            if s[length-2] != "0":
                checkNum = 2

    if bool(re.search(letters, s)):
        checkOne = 2

    if re.search(pattern, s):
        TorF -= 1

    if TorF == 2 and checkOne == 2 and checkNum == 2:
        return True
    


main()