import numpy as np


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
