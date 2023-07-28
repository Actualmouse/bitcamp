myArr = ["u","a","i","o","e","A","E","I","O","U"]

def main():
    inputTxt = shorten(str(input("Input text: ")))

    print(inputTxt)

def shorten(x):
    for char in range(10):
        x = x.replace(myArr[char], "")
    
    return x

main()