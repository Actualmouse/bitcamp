inputTxt = input("Camel: ")
final = inputTxt
counter = 0

for i in range(len(inputTxt)):
    x = inputTxt[i].isupper()
    
    counter += 1

    if x == True:
        outputTxt = inputTxt.index(inputTxt[i])
        
        replacedLetter = inputTxt[outputTxt]

        final = final.replace(replacedLetter, "_"+replacedLetter.lower())
    if x == len(inputTxt) and counter == 0:
        final = inputTxt
    
    
print(final)



    
   