#if demo
PWD = input("Enter password: ")
if PWD != "HELLO":
    print("Incorrect password")
    print("Program terminated")
if PWD == "HELLO":
    print("Correct password")
    print("Program continued...")