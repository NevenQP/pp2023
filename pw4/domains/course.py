import numpy as np


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
