#static variable
#static method
#class method.

class car:
    Static_var = 0 #static Variable
    def __init__(self, m, y, ma, mo):
        self.m = m
        self.y = y
        self.ma = ma
        self.mo = mo
        self.sample_list = []
        car.Static_var +=1

    def age(self, current_year):
        return current_year - self.y
    def append(self, a):
        self.sample_list.append(a)
        return self.sample_list

    def __str__(self):
        return "This is a string function which automatically called when object is simply called."

obj = car(20, 2020, 345324, "234fsdf")
print("Car Age: "+str(obj.age(2022)))
print(obj.append([1, 2, 3, 4, 5, 6]))

objects_list = [car(1, i, 234+i, "23232"+str(i)) for i in range(10)]
print(car.Static_var)
print(objects_list)
