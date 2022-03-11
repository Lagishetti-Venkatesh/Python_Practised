class iNeuron:
    num_of_courses = 12
    course_type = 'Machine-learning'
    def sample(self):
        print("This is ineuron class")


class Datascience(iNeuron):
    course_type = 'Data-Science'

    def sample(self):
        print('this is Data science class ')


class AI(Datascience):
    def __init__(self):
        self.company = "iNeuron"
        self.course_type = 'Deep-Learning'
        print('The company {0} offers total {1} different types of courses. Most trending course is {2}'.format(
            self.company, self.num_of_courses, self.course_type))
        self.sample()



AI = AI()