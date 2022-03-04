import logging as lg
import os

os.chdir(os.getcwd() + os.sep + "logging_debugging")
# Different Levels of logging the data .
lg.basicConfig(filename="test1.log", level=lg.DEBUG, format="%(asctime)s %(message)s", filemode="w")
# How to use withing a function
def divide(a, b):
    try:
        lg.info("This is Division function")
        lg.info("The input Data: {0}, {1}".format(a, b))
        result = a/b
        return result
    except Exception as e:
        lg.info("The information for Exception: {0}".format(e))

print(divide(9, 0))
lg.shutdown()


#second Example for Logging in function

def Summation(*args):
    lg.info("This is Summation function")
    sum = 0
    lg.info("sum = {}".format(sum))
    for i in args:
        lg.info("User input: {}".format(i))
        sum+=i
        lg.info("sum = {}".format(sum))
    return sum

if __name__ == "__main__":

    lg.info("This for Logging information")
    lg.warning("This is for warning")
    lg.debug("This is for debugging")
    lg.critical("This is for Critical")
    lg.error("This is for Error")

    print(divide(9, 0))

    print(Summation(1, 2, 3, 4, 5, 6, 7))

    print("Logged the Data Successfully")
    lg.shutdown()