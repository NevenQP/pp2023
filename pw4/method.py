import math
import curses

screen = curses.initscr()
curses.cbreak()
screen.keypad(True)


def round_to_1_decimal(a):
    return math.floor(10*a)/10


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


def sort_student_list_by_gpa(university):
    students = university.get_students()
    for i in range(len(students)):
            for j in range(0, len(students) - i - 1):
                if calculate_gpa(students[j]) > calculate_gpa(students[j + 1]):
                    temp = students[j]
                    students[j] = students[j + 1]
                    students[j + 1] = temp
    university.set_students(students)


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