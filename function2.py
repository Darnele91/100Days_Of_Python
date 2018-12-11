students = []


def getStudentsTitleCase():
    studentTitleCase = []
    for student in students:
        studentTitleCaase.append(student["name"].title())
    return studentTitleCase


def printStudentTitleCase():
    studentTitleCase = getStudentsTitleCase()
    print(studentTitleCase)


def addStudent(name, studentId):
    student = {"name" : name, "studentId" : studentId}
    students.append(student)

def saveFile(student):
    try:
        f = open("students.txt", "a")
        f.write(student + "\n")
        f.close()
    except Exception:
        print("Could not save file")


def readFile():
    try:
        f = open("students.txt", "r")
        for student in f.readlines():
            addStudent(student)
        f.close()
    except Exception:
        print("Could not read file")


readFile()
printStudentTitleCase()

studentName = input("Enter a name: ")
studentId = input("Enter Student ID: ")

addStudent(studentName, studentId)
saveFile(studentName)
