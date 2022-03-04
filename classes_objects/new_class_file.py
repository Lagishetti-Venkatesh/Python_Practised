class student:
    def __init__(self, name, rollno, joining_date, current_topic):
        self.name = name
        self.rollno = rollno
        self.joining_date = joining_date
        self.current_topic = current_topic

    def name_parsing(self):
        if type(self.name) == list:
            return [str(i) for i in self.name]

        else:
            return self.name

    def crt_topic(self):
        print("Today's Topic:"+ self.current_topic)

    def str_rollno(self):
        if type(self.rollno) == str:
            print("do something")
        else:
            return str(self.rollno)

    def durantion(self, current_date):
        print("Duration of Student: "+ str(current_date - self.joining_date))

    def __str__(self):
        return "This is a student class which handles the Data"

venky = student('srini', 5464, 2021, "OOP'S")
print(venky.str_rollno())
venky.durantion(2032)
sample = student(['srini', 'pawan', 'sample'], '5454', 2022, "oop's")
print(sample.name_parsing())
