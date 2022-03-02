def askForLength():
    length = input("Please enter the length of the array: ")
    if length.isdigit():
        return int(length)
    return askForLength()

def askForStart():
    start = input("Please enter the start of the array: ")
    if start.isdigit():
        return int(start)
    return askForStart()

def arrayIncrement(length  , start):
    arr =[]
    for i in range(length):
        if (len(arr)<length):
            print(i)
            arr.append(start+i)
    return arr

arrLen=askForLength()
arrStart=askForStart()
print(arrayIncrement(arrLen,arrStart))
    