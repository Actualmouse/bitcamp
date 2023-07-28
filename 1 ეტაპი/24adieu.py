myArr = []

def main():
    try:
        while True:
            user_input = input("name: ")        
            myArr.append(user_input)
            
    except EOFError:
        if len(myArr) == 2:
            string = " and " 
            print(f'Adieu, adieu, to {string.join(myArr)}')   
        elif len(myArr) == 1:
            string = ""
            print(f'Adieu, adieu, to {string.join(myArr)}')
        elif len(myArr) > 2:
            print("Adieu, adieu, to " + ", ".join(myArr[:-1]) + ", and " + myArr[-1])
    
main()