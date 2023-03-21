import curses
from method import *
from input import *
from output import *
from domains.university import *
from domains.course import *
from domains.student import *
from domains.mark import *

screen = curses.initscr()
curses.cbreak()
screen.keypad(True)

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
