check = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
check = check.lower()

if "42" in check or check == "forty-two" or check == "forty two":
    print("Yes")
else:
    print("No")
