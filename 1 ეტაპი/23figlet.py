from pyfiglet import Figlet
import sys

def main():     
    fontinput = check(input(""),input("Input: "))


def check(x,y):
    figlet = Figlet()
    allFonts = figlet.getFonts()
    fontArr = x.split()
    fontPrefix = ""
    fontValue = "big"


    if len(fontArr) == 2 or len(fontArr) == 0:
        if len(fontArr) == 2:
            fontPrefix = fontArr[0]
            fontValue = fontArr[1]
        
        if fontPrefix == "-f" or fontPrefix == "-font" and fontPrefix != "":
            ...
        else:
            exitSys()
    else: 
        exitSys()

    if fontValue in allFonts:
        figlet.setFont(font=fontValue)
        print(figlet.renderText(y))
    else:
        exitSys()

def exitSys():
    sys.exit("Invalid Usage")

main()