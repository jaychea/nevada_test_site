answer = ""
while answer not in ("1", "2"):
    answer = input("Did you eat breakfast today? (1/2)\n1) Yes, I ate breakfast today.\n2) No, I did not eat breakfast today.\n 1 or 2\n")
    if answer == "1":
        print("Good! It is the most important meal of the day.")
    elif answer == "2":
        print("It's okay. You were probably too busy sleeping.")
    else:
        print("Please enter 1 or 2. ")
