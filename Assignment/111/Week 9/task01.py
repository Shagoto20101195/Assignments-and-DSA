# Task 01

class Student:
    id_num = 0
    def __init__(self, name, dept, age, cgpa):
        Student.id_num += 1
        self.name = name
        self.dept = dept
        self.age = age
        self.cgpa = cgpa
        self.id = Student.id_num
    def get_details(self):
        print("ID:", self.id)
        print("Name:", self.name)
        print("Department:", self.dept)
        print("Age:", self.age)
        print("CGPA:", self.cgpa)
    @classmethod
    def from_String(cls, info):
        name, dept, age, cgpa = info.split("-")
        return cls(name, dept, age, cgpa)

s1 = Student("Samin", "CSE", 21, 3.91)
s1.get_details()
print("-----------------------")
s2 = Student("Fahim", "ECE", 21, 3.85)
s2.get_details()
print("-----------------------")
s3 = Student("Tahura", "EEE", 22, 3.01)
s3.get_details()
print("-----------------------")
s4 = Student.from_String("Sumaiya-BBA-23-3.96")
s4.get_details()

print()
print("Class variable are defined with the class constructor")
print("Class methods can modify class state and cannot modify object instance state")