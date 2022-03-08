import os
import logging as lg
from LogFunctions import get_logger

def func_one(lg_1):
    """
    Description:
        Sample function one for testing logging
    """
    lg_1.info("This Is the Function One")

def func_two(lg_2):
    """
    Description:
        Sample function one for testing logging
    """
    lg_2.info("This Is the Function TWO")

def func_three(lg_3):
    """
    Description:
        Sample function one for testing logging
    """
    lg_3.info("This Is the Function Three\n\n")
    print(Logging.count)

if __name__=="__main__":
    lg_1 = get_logger("log1")
    lg_2 = get_logger("log2")
    lg_3 = get_logger("log3")
    func_one(lg_1)
    func_two(lg_2)
    func_three(lg_3)
