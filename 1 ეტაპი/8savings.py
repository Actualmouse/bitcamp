userInput = input("Greeting: ")
userInput = userInput.lower()
noSpace = userInput.strip()

myArr = noSpace.split()

if myArr[0] == "hello":
    print("0$")
elif myArr[0][0] == "h":
    print("20$")
else:
    print("100$")





