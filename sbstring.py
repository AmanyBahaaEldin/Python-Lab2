def askForString():
    resultStr=""
    str = input("Please enter the string: ")
    if str.isalpha():
        resultStr=longest_alpha_substring(str)
        print(resultStr)
        return 
    return askForString()

def longest_alpha_substring(s):
    result = ''
    temporary_result = ''
    temporary_result = s[0]
    
    for i in range(len(s)-1):
        if s[i].lower()<=s[i+1].lower():
            temporary_result+=s[i+1]
        elif len(temporary_result)>len(result):
                result = temporary_result
                temporary_result = s[i+1]        
    if len(result)==0 or len(temporary_result)>len(result):
        result=temporary_result
    return result


askForString()
