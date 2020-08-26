def login():
    print("====Login====")

    usernames = []
    passwords = []
    with open("login.txt", "r") as f:
        for line in f:
            fields = line.strip().split(":")
            usernames.append(fields[0])  # read all the usernames into list usernames
            passwords.append(fields[1])  # read all the passwords into passwords list

            # Use a zip command to zip together the usernames and passwords to create a dict
    userinfo = zip(usernames, passwords)  # this is a variable that contains the dictionary in the 2-tuple list form
    userinfo_dict = dict(userinfo)
    print(userinfo_dict)

    username = input("Enter username:")
    password = input("Enter password:")

    if username in userinfo_dict.keys() and userinfo_dict[username] == password:
        loggedin()
    else:
        print("Access Denied")
        main()
login()
