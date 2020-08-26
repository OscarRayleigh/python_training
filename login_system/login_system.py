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
    f.write(username + " : " + password + "\n")
    print("\n Account succefully created ! ")
    main()
def login_account():
    username = input("Username : ")
    password = input("Password :")
    dictionary = {}
    with open("login.txt", "r") as file:
        for line in file:
            key, value = line.strip().split(":")
            dictionary[key] = value



main()
