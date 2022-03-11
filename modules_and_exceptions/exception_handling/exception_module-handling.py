from test_1 import mo1
from LogFunctions import get_logger


lg_data = get_logger("user1")
try:
    n = int(input("Enter the range: "))
    lg_data.info("User Input: {0}".format(n))
    even_numbers = mo1.even_num(n)

except Exception as e:
    lg_data.error("Exception occured is : {0}".format(e))

else:
    lg_data.info("The code Executed Successfully data: {0}".format(even_numbers))

finally:
    lg_data.info("Anyway you will execute the rest of the code.")