testString = ""
searchChar = ""
charList = []
lastPosition = -1


while testString == "":
    testString = raw_input("Please enter some text to search : ")

while len(searchChar) != 1:
    searchChar = raw_input("Enter a character to search for :")



for x in range (len(testString)):
    if testString[x] == searchChar:
        charList.append(x-lastPosition)
        lastPosition = x

print ("I found {0} occurences of {1}".format(len(charList),searchChar))

decision=raw_input("do you want to swap a character in that text? Y for yes, N for no: ")
if decision == ("Y"):
    change_to = ""
    while len(change_to) != 1:
        change_to = raw_input("what letter would you like to change it to? ")

    
    testString = testString.replace(searchChar,change_to)
 
    print ("The text is now: ",testString)
    
