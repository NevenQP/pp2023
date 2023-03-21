from method import *
import numpy as np
import curses
import curses.ascii
from domains.course import *
from domains.student import *
from domains.mark import *

screen = curses.initscr()
curses.cbreak()
screen.keypad(True)


def input_curses(string):
    screen.addstr(string)
    input_str = ""
    while True:
        c = screen.getch()
        if c == curses.KEY_ENTER or c == 10:
            break
        input_str += curses.ascii.unctrl(c)
    return input_str


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
