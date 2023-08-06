import random
from tabulate import tabulate

score = []

print("Welcome to the ROCK PAPER SCISSORS game!")
#ASCII ART COPIED FROM: https://emojicombos.com/rock-paper-scissors-ascii-art
print("""
⠀⠀⠀⠀⠀⣠⡴⠖⠒⠲⠶⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡴⠖⠒⢶⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⠁⠀⣀⠔⠁⠀⠀⠈⠙⠷⣤⠦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⠀⠀⢀⡿⠀⠀⠀⠀⠀⠀⠀
⣠⠞⠛⠛⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠘⢧⠈⢿⡀⢠⡶⠒⠳⠶⣄⠀⠀⠀⠀⠀⣴⠟⠁⠀⠀⠀⣰⠏⠀⢀⣤⣤⣄⡀⠀⠀
⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠛⠛⠃⠸⡇⠈⣇⠸⡇⠀⠀⠀⠘⣇⠀⠀⣠⡾⠁⠀⠀⠀⢀⣾⣣⡴⠚⠉⠀⠀⠈⠹⡆⠀
⣹⡷⠤⠤⠤⠄⠀⠀⠀⠀⢠⣤⡤⠶⠖⠛⠀⣿⠀⣿⠀⢻⡄⠀⠀⠀⢻⣠⡾⠋⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠀⠀⢀⣠⡾⠃⠀
⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡤⠖⠋⢀⣿⣠⠏⠀⠀⣿⠀⠀⠀⠘⠉⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⠀⣠⠶⠋⠁⠀⠀⠀
⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠋⠁⠀⠀⠠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠁⠀⠀⠀⢀⣴⡿⠥⠶⠖⠛⠛⢶⡄
⠀⠉⢿⡋⠉⠉⠁⠀⠀⠀⠀⠀⢀⣠⠾⠋⠀⠀⠀⠀⢀⣰⡇⠀⠀⢀⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⣠⠼⠃
⠀⠀⠈⠛⠶⠦⠤⠤⠤⠶⠶⠛⠋⠁⠀⠀⠀⠀⠀⠀⣿⠉⣇⠀⡴⠟⠁⣠⡾⠃⠀⠀⠀⠀⠀⠈⠀⠀⠀⣀⣤⠶⠛⠉⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣤⣀⣠⣤⠶⠶⠒⠶⠶⣤⣀⠀⠀⠀⢻⡄⠹⣦⠀⠶⠛⢁⣠⡴⠀⠀⠀⠀⠀⠀⣠⡶⠛⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠋⣠⠞⠋⠁⠀⠀⠀⠀⠙⣄⠀⠙⢷⡀⠀⠀⠻⣄⠈⢷⣄⠈⠉⠁⠀⠀⠀⢀⣠⡴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡾⠁⣴⠋⠰⣤⣄⡀⠀⠀⠀⠀⠈⠳⢤⣼⣇⣀⣀⠀⠉⠳⢤⣭⡿⠒⠶⠶⠒⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢸⠃⢰⠇⠰⢦⣄⡈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠛⠛⠓⠲⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠸⣧⣿⠀⠻⣤⡈⠛⠳⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠹⣆⠀⠈⠛⠂⠀⠀⠀⠀⠀⠀⠈⠐⠒⠒⠶⣶⣶⠶⠤⠤⣤⣠⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⢦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣦⣀⠀⠀⠀⠀⠐⠲⠤⣤⣀⡀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠶⠤⠤⠤⠶⠞⠋⠉⠙⠳⢦⣄⡀⠀⠀⠀⡷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠳⠦⠾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """)

def main():

    try:

        table = [['Start',1],['Exit',0]]
        headers = [f"Score: {len(score)}","Start the game"]
        print(tabulate(table, headers, tablefmt="heavy_grid"))
        ready = input("Select your choice: ")

        if ready == "0":
            print("You have left the game.")
            exit()
        elif ready == "1":
            print("The game has begun.")
            pass
        else:
            print("Unidentified input!")
            main()

        userMove = userChoice()
        botMove = botChoice()

        print(finalAnswer(userMove,botMove))
        print(f'Score: {len(score)}')

        input("CTRL+Z/CTRL+D here to exit, otherwise input anything.")
        main()
    except EOFError:
        exit()


def userChoice():
    try:
        #https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
        rock = ("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀_______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)

        paper = ("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀_______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)

        scissors = ("""
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀_______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

        table = [[rock,"Rock"],[paper,"Paper"],[scissors, "Scissors"]]
        headers = ["Choose","Your move"]
        print(tabulate(table, headers, tablefmt="heavy_grid"))
        userMove = input("Select your move: ")

        checkChoice(userMove)
        return userMove
    except EOFError:
        exit()

def checkChoice(x):
    try:
        x = str(x)
        if x.lower() == "scissors" or x.lower() == "rock" or x.lower() == "paper":
            print("Success")
        else:
            print("Invalid input!")
            userChoice()
    except EOFError:
        exit()

def botChoice():
    randNum = random.randint(1,3)

    if randNum == 1:
        return "rock"
    if randNum == 2:
        return "paper"
    if randNum == 3:
        return "scissors"


def finalAnswer(x,y):
    #x user
    #y bot
    x = str(x).lower()
    y = str(y).lower()

    #https://gist.github.com/wynand1004/b5c521ea8392e9c6bfe101b025c39abe
    rock = ("""
⠀⠀⠀⠀_______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

    paper = ("""
⠀⠀⠀⠀_______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

    scissors = ("""
⠀⠀⠀⠀_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

    myDic = {
        "rock" : rock,
        "paper" : paper,
        "scissors" : scissors
    }

    table = [[f"Your move: {myDic[x]}"],[f"Bot's move: {myDic[y]}"]]
    print(tabulate(table, tablefmt="heavy_grid"))

    if x == "rock" and y == "scissors":
        score.append("x")
        return "You won!"
    elif x == "rock" and y == "paper":
        return "You lost!"
    elif x == "scissors" and y == "rock":
        return "You lost!"
    elif x == "scissors" and y == "paper":
        score.append("x")
        return "You won!"
    elif x == "paper" and y == "rock":
        score.append("x")
        return "You won!"
    elif x == "paper" and y == "scissors":
        return "You lost!"
    elif x == y:
        return "Uh-oh! Thats a tie."


if __name__ == "__main__":
    main()