from LogFunctions import get_logger
class_log = get_logger('class')
class test:
    def __init__(self, a, b, c, d):
        self.__a = a
        self.b = b
        self.c = c
        self.d = d

    def custom_method(self, v):
        return v - self.__a

    def __str__(self):
        return "This is my test code for abstraction"

o = test(4, 5, 6, 7)
try:
    print(o.custom_method(7), o.__a)
except Exception as e:
    class_log.error("Exception e: {0}".format(e))

#INHERITANCE

class test1(test):
    def __init__(self, j, *args):
        super(test1, self).__init__(*args)
        self.j = j

m = test1(4, 5, 6, 7, 8)
print(m.b, m.j)
print(m.custom_method(90))
