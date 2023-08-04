def main():
    ogTime = convert(input("What time is it? "))

    if ogTime >= 7.0 and ogTime <= 8.0:
        print("breakfast time")
    elif ogTime >= 12.0 and ogTime <= 13.0:
        print("lunch time")
    elif ogTime >= 18.0 and ogTime <= 19.0:
        print("dinner time")


def convert(time):
    myArr = time.split(":")

    firstNum = float(myArr[0])
    secondNum = float(myArr[1])

    secondNum = secondNum/60

    value = firstNum+secondNum

    return value

if __name__ == "__main__":
    main()