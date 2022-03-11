class Ineuron:
    company_website = 'https://ineuron.ai/'
    name = 'iNeuron'

    def contact_details(self):
        print('Contact us at ', self.company_website)


class Datascience(Ineuron):
    def __init__(self):
        self.year_of_establishment = 2018

    def est_details(self):
        print('{0} Company was established in {1}'
              .format(self.name, self.year_of_establishment))


class OS:
    multi_task = True
    os_name = 'Windows OS'
    name = "sudh"


class windows(Ineuron, OS):
    def __init__(self):
        if self.multi_task is True:
            print('multi_task')
        print('Name: {}'.format(self.name))
        self.contact_details()


windows = windows()
