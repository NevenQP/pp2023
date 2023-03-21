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
