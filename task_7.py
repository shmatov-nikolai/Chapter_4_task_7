"""
7)Students room:

Implement Students room using OOP:
Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")
print(Steve)
<name: Steven Schultz, age: 23, major: English>
print(Johnny)
<name: Jonathan Rosenberg, age: 24, major: Biology>
"""

class Student():
    def __init__(self, name, surname, age, major):
        self.name = name
        self.surname = surname
        self.age = age
        self.major = major
    
    def __str__(self):
        return f"<name: {self.name.title()} {self.surname.title()}, age: {self.age}, major: {self.major.title()}>"


student_1 = Student('Nikolai', 'Shmatov', 31, 'Information technology')
student_2 = Student('bob', 'Marley', 55, 'travologiya')

print(student_1)
print(student_2)