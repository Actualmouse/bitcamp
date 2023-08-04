import emoji

def main():
    emojify(input("Input: "))

def emojify(x):
    print(emoji.emojize(x, language='alias'))

main()