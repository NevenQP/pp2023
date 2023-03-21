import numpy as np


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
