# When you enter in an invalid input for "Did you attend college?"
# The program loops back to the Age question (which comes prior to the college question).

name = input("Hello, what is your name? ")
print("Welcome to the NBA Draft Eligibility Board, " + name + ".")


def nba():
    while True:
        age = int(input("What is your age? "))
        if age < 19:
            print("You are not eligible for the NBA Draft.")
            break
        elif age >= 19 and age < 22:
            college = input("Did you attend college? (Y/N) ").upper()
            if college == "Y":
                print("You attended college, therefore you are eligible for the NBA Draft.")
                break
            elif college == "N":
                removed_hs = input("Are you at least one year removed from high school? (Y/N) ").upper()
                if removed_hs == "Y":
                    print("You have been one year removed from high school, therefore eligible for the NBA Draft.")
                    break
                elif removed_hs == "N":
                    print("You are not eligible for the NBA Draft.")
                    break
                else:
                    print("Please enter Y/N. ")
            else:
                print("Please enter Y/N. ")
        else:
            print("This person is more than eligible for the NBA draft.")
            break



nba()