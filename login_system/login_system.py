def main():
    print("\n Do you want to create an account or to login ?: \n")
    a = input("1. To create an account or 2. to login, 3. To exit : ")
    if a == "1":
        create_account()
    if a == "2":
        login_account()
    if a == "3":
        print("Exiting ...")
    elif a != "1" and a!= "2":
        print("something wrong happened")
        main()

def create_account():
    f = open("login.txt", "a")
    print("Creating account : \n")
    username = input("Username : ")
    password = input("Password :")
    if checker(username, password):
        f.write(username + ":" + password + " ")
        print("\n Account succefully created ! ")
        main()
    else:
        print("Error, choose an username please ")
        create_account()
def login_account():
    username = input("Username : ")
    password = input("Password :")
    if checker(username, password):
        verify_passwd(username, password)
    else:
        print("Error: You must choose an username ! (no space or no :) ")
        login_account()

def verify_passwd(username, password):
    with open('login.txt','r') as f:
        lines = f.readlines()
        my_dict = {}
        for line in lines:
            line = line.split(" ")
            print(line)

        print(my_dict) #create a dict and add each lines in it,
def checker(username, password):
    if username == "":
        return False
    if " " in username or " " in password:
        return False
    if ":" in username or ":" in password:
        return False
    else:
        return True
main()
