fullValue = 50

while 0 < fullValue:
    if fullValue != 0:
        inputValue = int(input("Insert Coin: "))

    if inputValue != 25 and inputValue != 10 and inputValue != 5:
        print(f"Amount Due: {fullValue}")
    elif inputValue == 25 or inputValue == 10 or inputValue == 5 and fullValue != 0:

        fullValue = fullValue-inputValue
        if fullValue > 0:
            print(f"Amount Due: {fullValue}")
        elif fullValue <= 0:
            fullValue = str(fullValue).replace("-", "")
            fullValue = int(fullValue)
            print(f"Change Owed: {fullValue}")
            break