import random

myArr = []
newArr = []

def main():
    counter = 0
    pts = 2
    level = get_level()

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        newArr.append(f"{x} + {y} = ")

    for i in range(10):
        if counter == 10:
            break

        answer = int(input(newArr[i]))
        splitArr = newArr[i].split(" ")

        alpha = int(splitArr[0])
        beta = int(splitArr[2])
        sum = alpha+beta

        if alpha + beta == answer:
            counter += 1
            pts += 1
        else:
            counter += 1
            print("EEE")
            answer = input(newArr[i])
            

            if alpha + beta == int(answer):
                counter += 1
                pts += 1
                
            else:
                
                print(f'{alpha} + {beta} = {sum}')
                










    print(pts)

    exit()



def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level != 1 and level != 2 and level != 3:
                raise ValueError
            return level
        except ValueError:
            level = int(input("Level: "))


def generate_integer(level):
    if level == 1:
        myArr = [0,9]
    elif level == 2:
        myArr = [10,99]
    elif level == 3:
        myArr = [100,999]

    randomNum = random.randrange(myArr[0],myArr[1])
    return randomNum

if __name__ == "__main__":
    main()