import hashlib, os
def main():
    print("Do you want to create an account or to login ?: \n")
    a = input("1. To create an account or 2. to login, 3. To exit : ")
    if a == "1":
        create_account()
    if a == "2":
        login()
    if a == "3":
        print("Exiting ...")
    elif a != "1" and a!= "2":
        print("Something wrong happened ")
        main()

def create_account():
    f = open("login.txt", "a")
    print("Creating account : \n")
    username = input("Username : ")
    password = input("Password : ")
    if checker(username, password):
        password_hash = hash_password(password)
        f.write(username + ":" + password_hash + "\n")
        print("\n Account succefully created ! ")
        f.close()
        main()
    else:
        print("Something wrong happened, you must not use a comma in your password or username ")
        create_account()
def login():
    print("============Login============ \n")
    usernames = []
    passwords = []
    with open("login.txt", "r") as f:
        for line in f:
            fields = line.strip().split(":")
            usernames.append(fields[0])
            passwords.append(fields[1])
    user_login = zip(usernames, passwords)
    login_dict = dict(user_login)
    username = input("Enter username: ")
    password = input("Enter password: ")
    if checker(username, password):
        if username in login_dict.keys() and login_dict[username] == password:
            loggedin()
        else:
            print("Access Denied\n")
            login()
    else:
        print("Something wrong happened, you must not use a comma in your password nor in your username ")

def checker(username, password):
    if "," in username or "," in password:
        return False
    else:
        return True
def loggedin():
    print("You just logged in ! ")
def hash_password(password):
    password_salt = os.urandom(32).hex()
    hash = hashlib.sha512()
    hash.update(('%s%s' % (password_salt, password)).encode('utf-8'))
    password_hash = hash.hexdigest()
    return password_hash
main()
