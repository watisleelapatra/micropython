#if demo
PWD = input("Enter password: ")
if PWD != "HELLO":
    print("Incorrect password")
    print("Program terminated")
else:
    print("Correct password")
    print("Program continued...")