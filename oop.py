# class jashwanth:
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age =age
#         self.course = course

# p1 = jashwanth("jashwanth", 21, "B.Tech")
# print(p1.name)
# print(p1.age)
# print(p1.course)
# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password

#     def login(self, u, p):
#         if self.username == u and self.password == p:
#             print("Login Successful")
#         else:
#             print("Invalid Credentials")

# user = User("admin", "1234")
# user.login("admin", "1234")
# class Temperature:
#     def celsius_to_fahrenheit(self, c):
#         return (c * 9/5) + 32

#     def fahrenheit_to_celsius(self, f):
#         return (f - 32) * 5/9

# t = Temperature()
# print(t.celsius_to_fahrenheit(30))
# print(t.fahrenheit_to_celsius(86))
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def annual_salary(self):
#         return self.salary * 12

# e = Employee("Kiran", 30000)
# print("Annual Salary:", e.annual_salary())

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def annual_salary(self):
#         return self.salary * 12

# e = Employee("Kiran", 30000)
# print("Annual Salary:", e.annual_salary())
print("hi ")
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compare(self, other):
        if self.marks > other.marks:
            print(self.name, "scored higher")
        else:
            print(other.name, "scored higher")

s1 = Student("A", 85)
s2 = Student("B", 80)

s1.compare(s2)
class Person:
    def __init__(self):
        self.__age = 0

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

p = Person()
p.set_age(21)
print(p.get_age())
class ATM:
    def __init__(self):
        self.__pin = 1234

    def validate_pin(self, pin):
        if pin == self.__pin:
            print("Access Granted")
        else:
            print("Wrong PIN")

atm = ATM()
atm.validate_pin(1234)