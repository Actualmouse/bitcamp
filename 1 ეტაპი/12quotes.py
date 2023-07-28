def main():
    x = int(input("Enter which program to use (1/2): "))

    if x == 1:

        print("What is the quote? These aren\'t the droids you\'re looking for.\n"+
        "Who said it? Obi-Wan Kenobi\n"+
        "Obi-Wan Kenobi says, \"These aren't the droids\n"+
        "you\'re looking for.\"")

    if x == 2:
        myArr = ["\"Know thy self, know thy enemy.\"",
                "\"Learn from yesterday, live for today, hope for tomorrow.\""]
        y = input("Whose quote do you want to hear? ")
        
        if y.lower() == "einstein":
            print(myArr[1])
        elif y.lower() == "sun tzu":
            print(myArr[0])
    

main()