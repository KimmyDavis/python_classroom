from classtools import Attr_Display
class Person(Attr_Display):
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def last_name(self):
        return self.name.split()[-1]
    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    # def __str__(self):
    #     statement = "[class: " + self.__class__.__name__
    #     for attr in self.__dict__.keys():
    #         statement += " " + attr + ": " + str(self.__dict__[attr])
    #     else:
    #         statement += "]"
    #     return statement
        # return "[%s: %s, %s, %s]" % (self.__class__.__name__, self.name, self.pay)
    
class Manager(Person):
    """
    A customised person with special requirements
    """
    def __init__(self, name, pay=0):
        super().__init__(name, "mgr", pay)
    def give_raise(self, percent, bonus=0.1):
        return super().give_raise(percent + bonus)
    
class Department:
    def __init__(self, *args):
        self.members = list(args)
    def add_member(self, person):
        self.members.append(person)
    def give_raises(self, percent):
        for member in self.members:
            member.give_raise(percent)
    def show_all(self):
        for member in self.members:
            print(member)



if __name__ == "__main__":
    davis = Person("Davis Kimmy")
    junior = Person("Junior Harry", job="coder", pay=100000)
    dave = Manager("dave", pay=1000)
    development = Department(davis, junior)
    development.add_member(dave)
    development.give_raises(.1)
    development.show_all()