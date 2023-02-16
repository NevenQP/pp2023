students = {}

courses = {}

marks = {}


def inputstudent():
    num_student = int(input("Enter the number of student in the class:"))
    for i in range(num_student):
        student_id = input("Enter the student id:")
        name = input("Enter the student name:")
        dob = input("Enter the student dob:")
        students[student_id] = {'name': name, 'dob': dob}


def inputcours():
    num_course = int(input("Enter the number of course in the class:"))
    for i in range(num_course):
        course_id = input("Enter the course id:")
        name = input("Enter the course name:")
        courses[course_id] = {'name': name}


def inputmark():
    course_id = input("Enter the course ID:")
    if course_id not in courses:
        print("Invalid id")
        return
    for student_id in students:
        mark = int(input(f"Enter student mark for {students[student_id]['name']}: "))
        if student_id not in marks:
            marks[student_id] = {}
        marks[student_id][course_id] = mark


def listcourse():
    for course_id in courses:
        print(f"{course_id}: {courses[course_id]['name']}")


def liststudent():
    for student_id in students:
        print(f"{student_id}: name:{students[student_id]['name']} dob:{students[student_id]['dob']}")


def listmark():
    course_id = input("Enter course id that you what to show student marks:")
    for student_id in students:
        print(f"{student_id} student:{students[student_id]['name']} mark:{marks[student_id][course_id]}")


print("Enter 1 to add students")
print("Enter 2 to add courses")
print("Enter 3 to add marks")
print("Enter 4 to show student list")
print("Enter 5 to show course list")
print("Enter 6 to show mark of all student in a course")
print("Enter 7 to exit")
while True:
    case = int(input("Enter the action:"))
    if case == 1:
        inputstudent()
    elif case == 2:
        inputcours()
    elif case == 3:
        inputmark()
    elif case == 4:
        liststudent()
    elif case == 5:
        listcourse()
    elif case == 6:
        listmark()
    elif case == 7:
        break
    else:
        print("Invalid")
