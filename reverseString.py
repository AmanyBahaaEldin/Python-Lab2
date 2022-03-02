def askForString():
    str = input("Please enter the string: ")
    if str.isalpha():
        return str
    return askForString()

def reverseString(strToReverse):
    return strToReverse [::-1]

string =askForString()
print(reverseString(string))