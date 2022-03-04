import os
from logging_Streamhandler import Logging
class data:
    def __init__(self, file_name, file_type, date, size ):
        self.file_name = file_name
        self.file_type = file_type
        self.date = date
        self.size = size
        lg_obj = Logging()
        self.lg = lg_obj.logging_setup()
    def __str__(self):
        return "This is file Handling class which opens file, reads and appends the Data to the existing file."

    def file_open(self):
        """
        Description:
            This function opens the file in write mode
            writes the predefined text.

        Input:
            Takes the file name.

        Output:
            returns the file with Newly written Text.
        """
        lg_open = self.lg.getLogger("file_open: ")
        data = "Hi this is venkatesh, I am Practising OOP's concepts right now. its fun to Practise. "
        try:
            with open(self.file_name, "w") as file:
                file.write(data)
                lg_open.info("Data written: {} ".format(data))
        except Exception as e:
                lg_open.error("Exception is: {}".format(e))

    def file_read(self):
        """
        Description:
            This function opens the file in read mode
            and displays the Text to the screen

        Input:
            Takes the Existing filename.

        Output:
            Displays the Data in the File.
        """
        lg_read = self.lg.getLogger("file_read: ")
        try:
            with open(self.file_name, "r") as file:
                for line in file.readlines():
                    data = line.strip()
                    lg_read.info("Read Data: {}".format(data))
                    print(data)
        except Exception as e:
                lg_read.error("Exception: ".format(e))

    def file_append(self, new_data):
        """
        Description:
            This function takes the new data and
            adds that data to the existing file.

        Input:
            new_data(str): Data which needs to be appended
                            for the existing file
        Output:
            will update the file with the new data.
        """
        lg_append = self.lg.getLogger("file_append: ")
        try:
           with open(self.file_name, "a") as file:
               lg_append.info("Appended Data: {}".format(new_data))
               file.write(new_data)
               print("Data written successfully")

        except Exception as e:
            lg_append("Exception: ".format(e))


if __name__ == "__main__":

    obj1 = data("venkat.txt", 'Text', "2022-02-02", 23)
    print(obj1)
    print("Opening the file....")
    obj1.file_open()
    print("reading the file data...\n")
    obj1.file_read()
    print("Appending the New Data...\n")
    obj1.file_append(" Sample Data which is added. ")
    print("Data from file After adding the New Data\n")
    obj1.file_read()