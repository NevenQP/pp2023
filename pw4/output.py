import curses
from method import *

screen = curses.initscr()
curses.cbreak()
screen.keypad(True)


def get_student_list_in_university(university):
    for student in university.get_students():
        screen.addstr("Student ID: " + student.get_student_id() + " Name: " + student.get_name() + " Dob: " + student.get_dob() + "\n")
    screen.getch()
    screen.clear()


def get_student_list_in_course(university, course_id):
    for student in get_course_by_id(university, course_id).get_students():
        screen.addstr("Student ID: " + student.get_student_id() + " Name: " + student.get_name() + " Dob: " + student.get_dob() + "\n")
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
