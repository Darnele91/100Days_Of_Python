students = []


class Student:
    schoolName = "Springfield High School"

    def __init__(self, name, studentId):
        self.name = name
        self.studentId = studentId
        students.append(self)

    def __str__(self):
        return "Student and ID: " + self.name + ", " + self.studentId

    def getNameCapitalize(self):
        return self.name.capitalize()

    def getSchoolName(self):
        return self.schoolName

class collegeStudent(Student):

	def getSchoolName(self):
		return "This is a College student"

	def getNameCapitalize(self):
		originalValue = super().getNameCapitalize()
		return originalValue + "-UMass"


student = collegeStudent("james", "123")
print(student.getNameCapitalize())
