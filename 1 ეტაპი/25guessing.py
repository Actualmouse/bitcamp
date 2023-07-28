import random

myArr = []

def main():
    randValue = randomize(input("Level: "))   
    myArr.append(randValue)
    recheck()

def recheck():
    check(input("Guess: "), myArr[0])

def randomize(x):
    x = int(x)
    if int(x) <= 0:
        main()
    else:
        chosen = random.randrange(1,x)
        return chosen
    
def check(x, z):
    x = int(x)
    z = int(z)
    if x > z:
        print("Too high!")
        recheck()
    elif x < z:
        print("Too low!")
        recheck()
    else:
        print("That's right")
        exit()

main()