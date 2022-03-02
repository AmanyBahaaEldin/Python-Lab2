
from os import read


def  readNum():
    numList=[]
    summ=0
    while True:
        inPut = input("Please enter the number: ")
        if inPut.isdigit():
            numList.append(int(inPut)) 
        elif inPut=="done":
            for i in range(len(numList)):
                summ+=numList[i]
            print(f"The total of numbers = {summ}")
            print(f"The count of numbers = {len(numList)}")
            print(f"The avarage of numbers = {summ/len(numList)}")
            break
        else:
            return readNum()
readNum()