print("Welcome to our new game")
# welcoming
name = input("Enter your name: ")


# --------------------
# function
def maths_game():
    marks = 0
    a = ["Add", "Sub", "Multiply"]
    print(a)
    b = input("Enter your Choice: ")
    # -----------
    # ADDITION
    if b == 'Add'.lower():
        print("\tYou choose 'Addition'\nWe will ask 5 question.\nEach carry 1M")
        # question 1
        qs1 = int(input("What is ans.\n50+190: "))
        if qs1 == 240:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 2
        qs2 = int(input("What is the answer.\n78 + 20: "))
        if qs2 == 98:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better again!")
            marks -= 1
        # question 3
        qs3 = int(input("What is the answer:\n90+120: "))
        if qs3 == 210:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better again!")
            marks -= 1
        # question 4
        qs4 = int(input("What is the answer:\n19+890: "))
        if qs4 == 909:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better again!")
            marks -= 1
        # question 5
        qs5 = int(input("What is the answer:\n56098+345: "))
        if qs5 == 56443:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better again!")
            marks -= 1
        print("\t~~~~~~~~Result~~~~~~~~")
        # Statement on marks
        print("Your total marks = ", marks)
        if marks == 5:
            print(f"Extermly good! {name}")
        elif marks == 4:
            print("Good job!")
        elif marks == 2:
            print("Fair!")
        else:
            print("Ok marks, You need more pratice")
            print('\n\tThank you for using my basic program')
            exit()
    # -----------------
    # SUBTRACT
    elif b == 'Sub'.lower():
        print("\tYou choose 'Subtract'\nWe will ask 5 question.\nEach carry 1M")
        # question 1
        qss1 = int(input("What is ans.\n70-24: "))
        if qss1 == 46:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 2
        qss2 = int(input("What is ans.\n109-106: "))
        if qss2 == 3:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 3
        qss3 = int(input("What is ans.\n895-785: "))
        if qss3 == 110:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 4
        qss4 = int(input("What is ans.\n190-50: "))
        if qss4 == 140:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 5
        qss5 = int(input("What is ans.\n5922-544: "))
        if qss5 == 5378:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # Statement on marks
        print("Your total marks = ", marks)
        if marks == 5:
            print(f"V.V.Good! {name}")
        elif marks == 4:
            print("Good job!")
        elif marks == 2:
            print("Fair!")
        else:
            print("Ok marks, You need more pratice")
            print('\n\tThank you for using my basic program')
            exit()
    # ----------------------------------------------------------------------------
    # Multiply
    elif b == 'Multiply'.lower():
        print("\tYou choose 'Subtract'\nWe will ask 5 question.\nEach carry 1M")
        # question 1
        qsm1 = int(input("What is ans.\n70*0: "))
        if qsm1 == 0:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 2
        qsm2 = int(input("What is ans.\n24*5: "))
        if qsm2 == 120:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 3
        qsm3 = int(input("What is ans.\n458*9: "))
        if qsm3 == 4122:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 4
        qsm4 = int(input("What is ans.\n18*6: "))
        if qsm4 == 108:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # question 5
        qsm5 = int(input("What is ans.\n8*69: "))
        if qsm5 == 552:
            print("Your answer is correct. You got 1M")
            marks += 1
        else:
            print("Your answer is wrong. You can do better!Try again!")
            marks -= 1
        # Resut
        print("Your total marks is ", marks, "Marks.")
        if marks == 5:
            print(f"VV good! {name}")
        elif marks == 4:
            print(F"Good! {name}")
        elif marks == 3:
            print(f"Fair! {name}")
        else:
            print("You can do at another time!")
    # statement
    else:
        print("Thank you for using our program")
        exit()


maths_game()