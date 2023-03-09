class Student:
    def __init__(self, studentId, n, dob):
        self.__studentId = studentId
        self.__name = n
        self.__dob = dob
        self.__marks = []

    def describe(self):
        print(f"Student ID:{self.__studentId}  Name:{self.__name}  Dob:{self.__dob}")

    def setId(self, studentId):
        self.__studentId = studentId

    def setName(self, name):
        self.__name = name

    def setDob(self, dob):
        self.__dob = dob

    def getName(self):
        return self.__name

    def getstudentID(self):
        return self.__studentId

    def getdob(self):
        return self.__dob

    def getMark(self):
        return self.__marks


class Course:
    def __init__(self, courseId, n):
        self.__courseId = courseId
        self.__name = n
        self.__students = []

    def addStudent(self, student):
        self.__students.append(student)

    def addMark(self, student_id, mark):
        for student in self.__students:
            if student_id == student.getstudentID():
                student.getMark().append({"course_id": self.__courseId, "mark": mark})

    def getStudentList(self):
        for student in self.__students:
            student.describe()

    def getMark(self):
        print(f"{self.__name} marks")
        for student in self.__students:
            for mark in student.getMark():
                if self.__courseId == mark["course_id"]:
                    print(f"Name:{student.getName()} Mark:{mark['mark']}")


Marc = Student(1, 'Marc', "10/1/2003")
Jest = Student(2, 'Jest', "11/2/2003")
Quad = Student(3, 'Quad', "12/3/2003")
Kate = Student(4, 'Kate', "13/4/2003")
Vali = Student(5, 'Vali', "14/5/2003")
Phys = Course(1, 'Physic')
Phys.addStudent(Marc)
Phys.addStudent(Jest)
Phys.addStudent(Quad)
Phys.addStudent(Kate)
Phys.addStudent(Vali)
Phys.addMark(1, 10)
Phys.addMark(2, 9)
Phys.addMark(3, 8)
Phys.addMark(4, 7)
Phys.addMark(5, 6)
Phys.getStudentList()
Phys.getMark()
