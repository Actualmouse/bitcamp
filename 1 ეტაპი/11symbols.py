count = input("What is your input string? ")
x = len(count)

if count == "":
    print("Please input")
    exit()
        

print(f"{count} has {x} characters.")