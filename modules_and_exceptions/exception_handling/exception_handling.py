
try:
    a = int(input("enter the number1: "))
    b = int(input("Enter the input number2: "))
    c = a/b
except: # if try fails it comes here.
    print("this block code works if try block fails")
else: # if try executed successfully it comes here.
    print("this will execute with success. if try block code works.")
finally:
    print("This will run in any circumstances.")
    l =[4, 5, 6, 7]
    print(l[0])

def askforint():
    while True:
        try:
            a = int(input("Enter an integer"))
        except Exception as e:
            print("This is the Error message: ", e)
        else:
            print("Person entered the data correctly")
            break
        finally:
            print("Close the Issue")


askforint()