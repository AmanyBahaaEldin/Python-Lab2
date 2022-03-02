def askForNum():
    num = input("Please enter the number: ")
    if num.isdigit():
        return int(num)
    return askForNum()


def fizzBuzz(num):
    result=""
    if (num%3==0) & (num%5!=0):
        result="Fizz"
    elif (num%3!=0) & (num%5==0):
        result="Buzz"
    elif (num%3==0) & (num%5==0):
        result="FizzBuzz"

    return result

number = askForNum()
print(fizzBuzz(number))
