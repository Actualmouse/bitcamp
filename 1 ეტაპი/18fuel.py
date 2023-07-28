def main():
    inputUser = check(input("Fraction: "))

def check(txt):
    try:
        myArr = txt.split("/")

        if not myArr[0].isdigit() or not myArr[1].isdigit():
            main()

        x = int(myArr[0])
        y = int(myArr[1])

        if x > y:
            main()

        if y == 0:
            main()

        z = (x/y)*100   
        rounded = round(z)
        
        if rounded <= 1:
            print("E")
            exit()
        elif rounded >= 99:
            print("F")
            exit()

        print(f'{rounded}%')


    except (ValueError, ZeroDivisionError):
        ...

main()