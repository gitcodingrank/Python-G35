print("-*-*--*-*-Welcome to My Notepad Application-*-*--*-*-")
str = input("Enter Text:  ")

def notepadMenu():
    print("1. To Find Text")
    print("2. To Replace Text")
    print("3. To Count The Char/Sequence")
    print("4. To Re-Input the Text")
    print("5. Exit")

while True:
    notepadMenu()
    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        text = input("Enter the Char/Sequence to Find: ")
        msg = ""
        if str.find(text)!=-1:
            msg = "Text is available in the original text."
        else:
            msg = "Text is not found."
        
        print("-------------------------------------------")
        print(msg)
        print("-------------------------------------------")
    elif choice == 2:
        replaceText = input("What to Replace: ")
        if str.find(replaceText)!=-1:
            replaceValue = input("Enter New Value for replacing: ")
            str = str.replace(replaceText, replaceValue)
            print("-------------------------------------------")
            print("Successfully replaced and below is the data after replacing.")
            print(str)
            print("-------------------------------------------")
        else:
            print("-------------------------------------------")
            print("Text is not available in the original String.")
            print("-------------------------------------------")
    elif choice == 3:
        #functionality for count
        pass
    elif choice == 4:
        #functionality for re-input.
        pass
    elif choice == 5:
        res = input("Do you want to exit(y/n): ")
        if res == 'y' or 'Y':
            print("Thank you for using my applicaiton.")
            break
    else:
        print("Invalid Choice, Please Try Again")
    
