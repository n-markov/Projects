x=2

try:
    #print(x/0)
    if not type(x) is str:
        raise TypeError("Only strings are allowed")
except NameError:
    print("Undefined.")
except ZeroDivisionError:
    print("Don't divide by 0.")
else:
    print("No errors!")
finally:
    print("Always going to print")

