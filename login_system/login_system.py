from cryptography.fernet import Fernet
import ast
import os.path
import os
import getpass

def main():
    print("============ Main Menu ============ \n")
    a = input(" 1. Create an account\n 2. Login \n 3. Reset keys \n 4. Exit \n")
    if a == "1":
        create_account()
    if a == "2":
        login()
    if a == "3":
        choice = input("Do you want to generate a new key ? Registered accounts will be lost \nPress y continue or anything else to abort : ")
        if choice == "y":
            os.remove("secret.key")
            os.remove("login.txt")
            generate_key()
            print("Key succefully reset, old accounts are now lost !")
            exit()
        else:
            print("Back to main menu ... ")
            main()
    if a == "4":
        print("See ya ...")
        exit()
    else:
        main()

def create_account():
    f = open("login.txt", "a")
    print("============ Creating account ============ \n")
    username = input("Username : ")
    password = getpass.getpass("Password : ")
    if username_is_available(username):
        if checker(username, password):
            f.write(username + ":" + str(encrypt_password(password)) + "\n")
            print("\n Account succefully created !\n ")
            f.close()
            main()
        else:
            print("Something wrong happened, space and colon are not allowed in usernames and \n colon in password")
            create_account()
    else:
        print("Username already in use ! ")
def login():
    print("============Login============ \n")
    empty_database_checker()
    usernames = []
    passwords = []
    f = open("login.txt", "r")
    for line in f:
        fields = line.strip().split(":")
        usernames.append(fields[0])
        passwords.append(fields[1])
    f.close()
    user_login = zip(usernames, passwords)
    login_dict = dict(user_login)
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if not username in usernames:
        print("ERROR : Account not in database. ")
        main()
    if checker(username, password):
        txt_password = decrypt_password(login_dict[username])
        if username in login_dict.keys() and txt_password.decode() == password:
            print("You just logged in ! Hello %s !!! " % (username))
            exit()
        else:
            print("Access Denied\n")
            login()
    else:
        print("Something wrong happened, you wrote char that cannot be in your password ")

def checker(username, password):
    if "," in username or "," in password or " " in username or not password or not username:
        return False
    else:
        return True

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_password(password):
    key = load_key()
    encoded_password = password.encode()
    f = Fernet(key)
    encrypted_password = f.encrypt(encoded_password)
    return encrypted_password

def decrypt_password(encrypted_password_str):
    encrypted_password_byte = ast.literal_eval(encrypted_password_str)
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password_byte)
    return decrypted_password

def username_is_available(username):
    usernames = []
    with open("login.txt", "r") as f:
        for line in f:
            fields = line.strip().split(":")
            usernames.append(fields[0])
        if username in usernames:
            return False
        else:
            return True
def empty_database_checker():
    if os.path.isfile('./login.txt') == False or os.stat("login.txt").st_size == 0:
        print("ERROR ! : Data base empty ... ")
        main()

if os.path.isfile('./secret.key') == False:
    generate_key()

print(r"""\

Welcome to :
          _   _  _______          ____  __
    /\   | \ | |/ ____\ \        / /  \/  |   /\
   /  \  |  \| | (___  \ \  /\  / /| \  / |  /  \
  / /\ \ | . ` |\___ \  \ \/  \/ / | |\/| | / /\ \
 / ____ \| |\  |____) |  \  /\  /  | |  | |/ ____ \
/_/    \_\_| \_|_____/    \/  \/   |_|  |_/_/    \_\

    "A Very Not Secured Way to Manage Account"
                                                    """)

main()
