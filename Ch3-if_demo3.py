#if demo
User = input("Enter username: ")
PWD = input("Enter password: ")
if User != "admin" or PWD != "HELLO":
    print("Incorrect user or password")
    print("Program terminated")
if User == "admin" and PWD == "HELLO":
    print("User accepted")
    print("Program continued...")