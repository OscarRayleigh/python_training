from cryptography.fernet import Fernet
import ast
import os.path

def main():
    print("============ Main Menu ============ \n")
    a = input(" 1. Create an account\n 2. Login \n 3. Reset keys \n 4. Exit \n")
    if a == "1":
        create_account()
    if a == "2":
        login()
    if a == "3":
        choice = input("Do you want to generate a new key ? y for yes : ")
        if choice == "y":
            os.remove("secret.key")
            generate_key()
            main()
        else:
            print("Back to main menu ... ")
            main()
    if a == "4":
        print("See ya ...")
        exit()
    else:
        print("Something wrong happened ")
        main()

def create_account():
    f = open("login.txt", "a")
    print("============ Creating account ============ \n")
    username = input("Username : ")
    password = input("Password : ")
    if username_available(username):
        if checker(username, password):
            f.write(username + ":" + str(encrypt_message(password)) + "\n")
            print("\n Account succefully created ! ")
            f.close()
            main()
        else:
            print("Something wrong happened, space and colon are not allowed in usernames and \n colon in password")
            create_account()
    else:
        print("Username already in use ! ")
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
    txt_password = decrypt_message(login_dict[username])

    if checker(username, password):
        if username in login_dict.keys() and txt_password.decode() == password:
            print("You just logged in ! Hello %s !!! " % (username))
            exit()
        else:
            print("Access Denied\n")
            login()
    else:
        print("Something wrong happened, you wrote char that cant be in your password ")

def checker(username, password):
    if "," in username or "," in password or " " in username:
        return False
    else:
        return True

def generate_key():

    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():

    return open("secret.key", "rb").read()

def encrypt_message(password):

    key = load_key()
    encoded_message = password.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)
    return encrypted_message

def decrypt_message(encrypted_password_str):

    encrypted_password_byte = ast.literal_eval(encrypted_password_str)
    key = load_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password_byte)
    return decrypted_password

def username_available(username):
    usernames = []
    with open("login.txt", "r") as f:
        for line in f:
            fields = line.strip().split(":")
            usernames.append(fields[0])
        if username in usernames:
            return False
        else:
            return True

if os.path.isfile('./secret.key') == False:
    generate_key()
main()
