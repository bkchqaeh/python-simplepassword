attempts = 3

while attempts < 4:
    password = input("\n  Enter password : ")
    if password == "123321":
        print("\n    Nuclear launch codes.")
        break
    else:
        attempts -= 1
        print(f"\n    Invalid password. {attempts} Attempts left.")

    if attempts == 0:
        print("\n    You are blocked.")
        break
