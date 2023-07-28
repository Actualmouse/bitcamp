userInput = input("File name: ").lower()
myArr = userInput.split(".")
length = len(myArr)-1
myArr[length] = myArr[length].replace(" ","")

if len(myArr) == 0:
    print('application/octet-stream')
if myArr[length] == "gif":
    print("image/gif")
elif myArr[length] == "jpg" or myArr[length] == "jpeg":
    print("image/jpeg")
elif myArr[length] == "png":
    print('image/png')
elif myArr[length] == "pdf":
    print("application/pdf")
elif myArr[length] == "txt":
    print("text/plain")
elif myArr[length] == 'zip':
    print('application/zip')
else:
    print("application/octet-stream")