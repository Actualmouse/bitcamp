def main():
    userInput = value(input("Greeting: "))
    print(userInput)

def value(greeting):
    greeting = greeting.lower()
    noSpace = greeting.strip()

    myArr = noSpace.split()

    if "hello" in myArr[0]:
        return "$0"
    elif myArr[0][0] == "h":
        return "$20"
    else:
        return "$100"

if __name__ == "__main__":
    main()