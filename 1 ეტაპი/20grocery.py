myDict = {}
try:
    while True:
        userInput = input("")
        if not userInput:
            break

        userInput = userInput.lower()  # Convert the input to lowercase

        if userInput in myDict:
            myDict[userInput] += 1
        else:
            myDict[userInput] = 1

except EOFError:
    sorted_items = sorted(myDict.items(), key=lambda x: x[0])  # Sort items based on keys

    for key, value in sorted_items:
        print(f"{myDict[key]} {key.upper()}")
