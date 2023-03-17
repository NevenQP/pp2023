class Mark:
    def __init__(self, course_id, course_name, mark):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__mark = mark

    def set_mark(self, mark):
        self.__mark = mark

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_course_name(self, course_name):
        self.__course_name = course_name

    def get_course_id(self):
        return self.__course_id

    def get_mark(self):
        return self.__mark

    def get_course_name(self):
        return self.__course_name


class Student:
    def __init__(self, student_id, n, dob):
        self.__student_id = student_id
        self.__name = n
        self.__dob = dob
        self.__marks = []

    def describe(self):
        print(f"Student ID:{self.__student_id}  Name:{self.__name}  Dob:{self.__dob}")

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_name(self, name):
        self.__name = name

    def set_dob(self, dob):
        self.__dob = dob

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_dob(self):
        return self.__dob

    def get_marks(self):
        return self.__marks

    def get_mark(self):
        for mark in self.__marks:
            print(f"{mark.get_course_id()} {mark.get_course_name()} {mark.get_mark()}")


class Course:
    def __init__(self, course_id, n):
        self.__course_id = course_id
        self.__course_name = n
        self.__students = []

    def describe(self):
        print(f"Course ID:{self.__course_id}  Name:{self.__course_name}")

    def add_student(self, student):
        self.__students.append(student)

    def add_mark(self, student_id, mark):
        if mark < 0 or mark > 20:
            print(f"Invalid mark for id {student_id}")
            return
        for student in self.__students:
            if student_id == student.get_student_id():
                student.get_marks().append(Mark(self.__course_id, self.__course_name, mark))

    def get_student_list(self):
        for student in self.__students:
            student.describe()

    def get_course_marks(self):
        for student in self.__students:
            for mark in student.get_marks():
                if self.__course_id == mark.get_course_id():
                    print(f"Name:{student.get_name()} Mark:{mark.get_mark()}")


class University:
    def __init__(self, name):
        self.__university_name = name
        self.__students = []
        self.__courses = []

    def add_student(self, student):
        self.__students.append(student)

    def add_course(self, course):
        self.__courses.append(course)

    def get_student_list(self):
        for student in self.__students:
            student.describe()

    def get_course_list(self):
        for course in self.__courses:
            course.describe()


USTH = University("USTH")
Marc = Student(1, 'Marc', "10/1/2003")
Jest = Student(2, 'Jest', "11/2/2003")
Quad = Student(3, 'Quad', "12/3/2003")
Kate = Student(4, 'Kate', "13/4/2003")
Vali = Student(5, 'Vali', "14/5/2003")
Phys = Course(1, 'Physic')
Math = Course(2, 'Math')
Phys.add_student(Marc)
Phys.add_student(Jest)
Phys.add_student(Quad)
Phys.add_student(Kate)
Phys.add_student(Vali)
USTH.add_student(Marc)
USTH.add_student(Jest)
USTH.add_student(Quad)
USTH.add_student(Kate)
USTH.add_student(Vali)
USTH.add_course(Phys)
USTH.add_course(Math)
USTH.get_student_list()
USTH.get_course_list()
Phys.add_mark(1, 20)
Phys.add_mark(2, 9)
Phys.add_mark(3, 8)
Phys.add_mark(4, 7)
Phys.add_mark(5, 6)
Math.add_student(Marc)
Math.add_mark(1, 8)
Phys.get_student_list()
Phys.get_course_marks()
Marc.get_mark()
