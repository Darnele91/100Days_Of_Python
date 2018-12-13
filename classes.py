students = []


class Student:
    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId
        students.append(self)

    def __str__(self):
        return "Student and ID: " + self.name + ", " + self.studentId

    def getNameCapitalize(self):
        return self.name.capitalize()


student = Student("Darnele", "123")
print(student)
