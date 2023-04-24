#i = 3
#x = 1
#for a in range(1, i+1):
#    x *= a
#    print(x)

#n! = n * (n-1)

def factorial(number):
    if number == 1 or 0:
        return 1
    else:
        return number * factorial(number-1)
i = int(input("Enter the number: "))
fac = factorial(i)
print(f"--> {fac}")
factorial(fac)
