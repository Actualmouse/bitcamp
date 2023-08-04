def main():
    userInput = convert(input("Fraction: "))
    gauge(userInput)


def convert(fraction):
    try:
        myArr = fraction.split("/")
        if not myArr[0].isdigit() or not myArr[1].isdigit():
            main()
        x = int(myArr[0])
        y = int(myArr[1])
        z = (x/y)*100
        rounded = round(z)

        if x > y:
            main()

        if y == 0:
            main()

        return int(rounded)
    except (ValueError, ZeroDivisionError, TypeError):
        pass


def gauge(percentage):
    try:
        if percentage <= 1:
                print("E")
                exit()
        elif percentage >= 99:
            print("F")
            exit()

        print(f'{percentage}%')
    except (ValueError, ZeroDivisionError, TypeError):
        main()

if __name__ == "__main__":
    main()