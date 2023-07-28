exp = input("Expression: ")
myArr = exp.split()


x = myArr[0]
y = myArr[1]
z = myArr[2]



if y == "+":
    print(int(x)+int(z))
elif y == "-":
    print(int(x)-int(z))
elif y == "/":
    print(int(x)/int(z))
elif y == "*":
    print(int(x)*int(z))