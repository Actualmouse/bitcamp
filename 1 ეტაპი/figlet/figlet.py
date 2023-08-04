from pyfiglet import Figlet
import sys

def sysexit():
    sys.exit(1)

def main():
    if len(sys.argv) == 1:
        font_name = None
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        font_name = sys.argv[2]
    else:
        sysexit()

    try:
        figlet = Figlet(font=font_name) if font_name else Figlet()
    except ValueError:
        sysexit()

    text = input("Text ")
    print(figlet.renderText(text))

main()