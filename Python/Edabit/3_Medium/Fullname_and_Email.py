# 20200830 - Fullname and Email
class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = self.firstname + " " + self.lastname
        self.email = self.firstname.lower() + "." + self.lastname.lower() + "@company.com"

    def other_test(self):
        return self.email
"""
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname
emp_2.email
emp_3.firstname
"""
emp_1 = Employee("John", "Smith")
print(emp_1.other_test())