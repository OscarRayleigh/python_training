from cryptography.fernet import Fernet
import ast

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
        f.write(username + ":" + str(encrypt_message(password)) + "\n")
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
    txt_password = decrypt_message(login_dict[username])

    if checker(username, password):
        if username in login_dict.keys() and txt_password.decode() == password:
            loggedin()
        else:
            print("Access Denied\n")
            print(txt_password)
            print(password)
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



if input("Do you want to generate a new key ? ") == "y":
    generate_key()
main()
