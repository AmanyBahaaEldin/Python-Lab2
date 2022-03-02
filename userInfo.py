import re
user={"name":"" , "email":""}


mail=r'\b[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def askForEmail():
    email = input("Please enter your email: ")
    if(re.fullmatch(mail,email)):
        user["email"]=email
        return True
    else:
        print("Enter valid email...")
        return askForEmail()

def askForData():
    usrName = input("Please enter your name: ")
    if usrName.isalpha():
        print("^__^ entered valid name .... let's proceed")
        user["name"]=usrName
        if(askForEmail()):
            print(f"your name: {user['name']} , and your email: {user['email']}")
        return
    return askForData()

askForData()