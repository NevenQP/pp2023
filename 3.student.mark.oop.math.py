import math
import numpy as np
import curses
import curses.ascii

screen = curses.initscr()
curses.cbreak()
screen.keypad(True)


class Mark:
    def __init__(self, course_id, course_name, credit, mark):
        self.__course_id = course_id
        self.__course_name = course_name
        self.__credit = credit
        self.__mark = mark

    def set_mark(self, mark):
        self.__mark = mark

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_course_name(self, course_name):
        self.__course_name = course_name

    def set_credit(self, credit):
        self.__credit = credit

    def get_course_id(self):
        return self.__course_id

    def get_mark(self):
        return self.__mark

    def get_course_name(self):
        return self.__course_name

    def get_credit(self):
        return self.__credit


class Student:
    def __init__(self, student_id, n, dob):
        self.__student_id = student_id
        self.__name = n
        self.__dob = dob
        self.__marks = np.array([])

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def set_name(self, name):
        self.__name = name

    def set_dob(self, dob):
        self.__dob = dob

    def set_mark(self, mark):
        self.__marks = mark

    def get_name(self):
        return self.__name

    def get_student_id(self):
        return self.__student_id

    def get_dob(self):
        return self.__dob

    def get_marks(self):
        return self.__marks


class Course:
    def __init__(self, course_id, name, credit):
        self.__course_id = course_id
        self.__name = name
        self.__credit = credit
        self.__students = np.array([])

    def set_course_id(self, course_id):
        self.__course_id = course_id

    def set_name(self, name):
        self.__name = name

    def set_credit(self, credit):
        self.__credit = credit

    def get_name(self):
        return self.__name

    def get_course_id(self):
        return self.__course_id

    def get_credit(self):
        return self.__credit

    def add_student(self, student):
        self.__students = np.append(self.__students, student)

    def get_students(self):
        return self.__students


class University:
    def __init__(self, name):
        self.__university_name = name
        self.__students = np.array([])
        self.__courses = np.array([])

    def add_student(self, student):
        self.__students = np.append(self.__students, student)

    def add_course(self, course):
        self.__courses = np.append(self.__courses, course)

    def set_students(self, students):
        self.__students = students
    
    def set_courses(self, courses):
        self.__courses = courses

    def get_students(self):
        return self.__students
    
    def get_courses(self):
        return self.__courses


def input_curses(string):
    screen.addstr(string)
    input_str = ""
    while True:
        c = screen.getch()
        if c == curses.KEY_ENTER or c == 10:
            break
        input_str += curses.ascii.unctrl(c)
    return input_str


def get_student_by_id(university,student_id):
    for student in university.get_students():
        if student_id == student.get_student_id():
            return student
    return False


def get_course_by_id(university,course_id):
    for course in university.get_courses():
        if course_id == course.get_course_id():
            return course
    return False


def input_student():
    student_id = input_curses("Enter the student id:")
    name = input_curses("Enter the student name:")
    dob = input_curses("Enter the student dob:")
    screen.clear()
    return Student(student_id, name, dob)


def input_course():
    course_id = input_curses("Enter the course id:")
    course_name = input_curses("Enter the course name:")
    credit = int(input_curses("Enter the course credit:"))
    screen.clear()
    return Course(course_id, course_name, credit)


def add_students_to_university(university):
    num_student = int(input_curses("Enter the number of student:"))
    screen.clear()
    for i in range(num_student):
        university.add_student(input_student())


def add_courses_to_university(university):
    num_course = int(input_curses("Enter the number of course:"))
    screen.clear()
    for i in range(num_course):
        university.add_course(input_course())


def add_student_from_university_to_course(university):
    course_id = input_curses("Enter the course id to add student:")
    if get_course_by_id(university, course_id) is False:
        screen.addstr("Invalid course")
        screen.getch()
        screen.clear()
        return
    
    num_student = int(input_curses("Enter the number of student:"))
    for i in range(num_student):
        student_id = input_curses("Enter the student id:")
        if get_student_by_id(university, student_id) is False:
            screen.addstr("Invalid student")
            screen.getch()
            screen.clear()
            return
        get_course_by_id(university, course_id).add_student(get_student_by_id(university, student_id))
    screen.clear()


def add_mark(university):
    course_id = input_curses("Enter the course id to add mark:")
    if get_course_by_id(university, course_id) is False:
        screen.addstr("Invalid course")
        screen.getch()
        screen.clear()
        return
    
    course = get_course_by_id(university,course_id)
    for student in course.get_students():
        while True:
            mark = round_to_1_decimal(int(input_curses(f"Enter mark of student {student.get_student_id()}:")))
            if mark < 0 or mark > 20:
                screen.addstr(f"Invalid mark for id {student.get_student_id()}")
                screen.getch()
                screen.clear()
                return
            break
        
        student.set_mark(np.append(student.get_marks(), Mark(course_id, course.get_name(), course.get_credit(),mark)))
    screen.clear()


def round_to_1_decimal(a):
    return math.floor(10*a)/10


def get_student_list_in_university(university):
    for student in university.get_students():
        screen.addstr("Student ID: " + student.get_student_id() + " Name: " + student.get_name() +  " Dob: " + student.get_dob() + "\n")
    screen.getch()
    screen.clear()


def get_student_list_in_course(university, course_id):
    for student in get_course_by_id(university, course_id).get_students():
        screen.addstr("Student ID: " + student.get_student_id() + " Name: " + student.get_name() +  " Dob: " + student.get_dob() + "\n")
    screen.getch()
    screen.clear()


def get_course_list(university):
    for course in university.get_courses():
        screen.addstr("Course ID: " + course.get_course_id() + " Name: " + course.get_name() + "\n")
    screen.getch()
    screen.clear()


def get_student_mark(university, student_id):
    for mark in get_student_by_id(university, student_id).get_marks():
        screen.addstr("Course ID: " + mark.get_course_id() + " Name: " + mark.get_course_name() + " Mark: " + str(mark.get_mark()) +"\n")
    screen.getch()
    screen.clear()


def get_course_marks(university, course_id):
    for student in university.get_students():
        for mark in student.get_marks():
            if course_id == mark.get_course_id():
                screen.addstr("Name: " + student.get_name() + " Mark: " + str(mark.get_mark()) + "\n")
    screen.getch()
    screen.clear()


def calculate_wam(student):
    total_mark = 0
    total_credit = 0
    for mark in student.get_marks():
        total_mark += mark.get_mark() * mark.get_credit()
        total_credit += mark.get_credit()
    if total_credit == 0:
        return 0
    wam = total_mark/total_credit
    return round_to_1_decimal(wam)


def calculate_gpa(student):
    pass_limit = 10
    total_mark = 0
    total_credit = 0
    for mark in student.get_marks():
        if mark.get_mark() >= pass_limit:
            total_mark += mark.get_mark() * mark.get_credit()
        total_credit += mark.get_credit()
    if total_credit == 0:
        return 0
    gpa = total_mark/total_credit
    return round_to_1_decimal(gpa)


def get_students_gpa(university):
    for student in university.get_students():
        screen.addstr("Student ID: " + student.get_student_id() + " Name: " + student.get_name() + " GPA: " + str(calculate_gpa(student)) + "\n")
    screen.getch()
    screen.clear()


def get_students_wam(university):
    for student in university.get_students():
        screen.addstr("Student ID: " + student.get_student_id() + " Name: " + student.get_name() + " WAM: " + str(calculate_wam(student)) + "\n")
    screen.getch()
    screen.clear()


def sort_student_list_by_gpa(university):
    students = university.get_students()
    for i in range(len(students)):
            for j in range(0, len(students) - i - 1):
                if calculate_gpa(students[j]) > calculate_gpa(students[j + 1]):
                    temp = students[j]
                    students[j] = students[j + 1]
                    students[j + 1] = temp
    university.set_students(students)


USTH = University("USTH")

while True:
    screen.addstr("Enter 1 to add students \n")
    screen.addstr("Enter 2 to add courses \n")
    screen.addstr("Enter 3 to add students to course \n")
    screen.addstr("Enter 4 to add mark \n")
    screen.addstr("Enter 5 to show student list in university \n")
    screen.addstr("Enter 6 to show student list in course \n")
    screen.addstr("Enter 7 to show course list \n")
    screen.addstr("Enter 8 to show mark of specific student \n")
    screen.addstr("Enter 9 to show mark of all student in a course \n")
    screen.addstr("Enter 10 to show gpa of all student in a course \n")
    screen.addstr("Enter 11 to show wam of all student in a course \n")
    screen.addstr("Enter 12 to sort student list by gpa \n")
    screen.addstr("Enter 13 to exit \n")
    case = int(input_curses("Enter the action: \n"))
    screen.clear()
    if case == 1:
        add_students_to_university(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 2:
        add_courses_to_university(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 3:
        add_student_from_university_to_course(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 4:
        add_mark(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 5:
        get_student_list_in_university(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 6:
        course_id = input_curses("Enter the course id:")
        get_student_list_in_course(USTH, course_id)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 7:
        get_course_list(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 8:
        student_id = input_curses("Enter the student id:")
        get_student_mark(USTH, student_id)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 9:
        course_id = input_curses("Enter the course id:")
        get_course_marks(USTH, course_id)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 10:
        get_students_gpa(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 11:
        get_students_wam(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 12:
        sort_student_list_by_gpa(USTH)
        screen.addstr("Done")
        screen.getch()
        screen.clear()
    elif case == 13:
        curses.nocbreak()
        screen.keypad(False)
        curses.endwin()
        break
    else:
        screen.addstr("Invalid")
        screen.getch()
        screen.clear()
