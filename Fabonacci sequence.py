print("Welcome to fibonacci seequence")

def fibo():
    """
    This program help you find fibonacci number,
    and this program dosen't take two value.
    """
    print(fibo.__doc__)
    a = int(input("Enter the number: "))
    f = a - 1 + a - 2
    print("Hence, Your answer is: ", f)

    while True:
        x = "Yes"
        y = "No"
        print("Yes")
        print("No")
        r = input("Do you want to continue the program: ")
        if r == "Yes":
             fibo()
        elif r == "No":
            exit()
fibo()