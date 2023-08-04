from validator_collection import checkers


isMail = checkers.is_email(input("What's your E-Mail? "))
if isMail == True:
    answer = "Valid"
elif isMail == False:
    answer = "Invalid"

print(answer)