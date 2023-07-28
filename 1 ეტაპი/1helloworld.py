code = int(input("Which code do you want to run? (1/2/3): "))

if code == 3:
    #no variable
    print("Hello " + input("Whats your name? "))
elif code == 2:
    #with variable
    username = input("What's your name? ")
    print(f"Hello there {username}!")
elif code == 1:
    #different responses
    name = input("What's your name? ")
    if name.lower() == "leqso":
        print("What's up Lexy, im sexy")
    elif name[0].lower() == "g":
        print(f"GGGGGamarjoba {name}")