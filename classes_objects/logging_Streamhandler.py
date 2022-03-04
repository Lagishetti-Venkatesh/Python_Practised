import os
import logging as lg
class Logging:
    count = 0 #Static Variable
    def __init__(self):
        Logging.count+=1

    def logging_setup(self):
        """
        Description:
            This function is used for setting up the logging process

        Input:
            Nothing.

        Output:
            returns a logging object which can be used for creating the various users logs.
        """
        # changing To current directory.
        os.chdir(os.getcwd())

        lg.basicConfig(filename="programFlowData.log", level=lg.DEBUG,
                       format="%(name)s %(asctime)s %(levelname)s %(message)s", filemode="w")
        #creating Handlers
        console_log = lg.StreamHandler()
        console_log.setLevel(lg.DEBUG)
        format = "%(name)s %(asctime)s %(levelname)s %(message)s"
        console_log.setFormatter(format)

        #creating Custom Logger
        lg.getLogger('').addHandler(console_log)
        print("Logging Setup done. Logging data will be saved in programFlowData.log")

        return lg

def func_one():
    """
    Description:
        Sample function one for testing logging
    """
    lg = Logging()
    lg_1 = lg.logging_setup().getLogger("User1")
    lg_1.info("This Is the Function One")

def func_two():
    """
    Description:
        Sample function one for testing logging
    """
    lg = Logging()
    lg_2 = lg.logging_setup().getLogger("User2")
    lg_2.info("This Is the Function TWO")

def func_three():
    """
    Description:
        Sample function one for testing logging
    """
    lg = Logging()
    lg_3 = lg.logging_setup().getLogger("User3")
    lg_3.info("This Is the Function Three\n\n")
    print(Logging.count)

if __name__=="__main__":
    func_one()
    func_two()
    func_three()