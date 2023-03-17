students = []

courses = []

marks = [{"student_id": 'none'}]


def input_student():
    num_student = int(input("Enter the number of student in the class:"))
    for i in range(num_student):
        student_id = input("Enter the student id:")
        name = input("Enter the student name:")
        dob = input("Enter the student dob:")
        students.append({'student_id': student_id, 'name': name, 'dob': dob})


def input_course():
    num_course = int(input("Enter the number of course in the class:"))
    for i in range(num_course):
        course_id = input("Enter the course id:")
        name = input("Enter the course name:")
        courses.append({'course_id': course_id, 'name': name})


def input_mark():
    course_id = input("Enter the course id:")
    exist = False
    for i in range(len(courses)):
        if course_id == courses[i]['course_id']:
            exist = True
            break

    if exist is False:
        print("Invalid id")
        return

    for student in students:
        exist = False
        mark = int(input(f"Enter student mark for {student['name']}: "))
        for i in range(len(marks)):
            if student['student_id'] == marks[i]['student_id']:
                marks[i][course_id] = mark
                exist = True
                break
        if exist is False:
            marks.append({'student_id': student['student_id'], course_id: mark})


def list_course():
    for course in courses:
        print(f"{course['course_id']}: {course['name']}")


def list_student():
    for student in students:
        print(f"{student['student_id']}: name:{student['name']} dob:{student['dob']}")


def list_mark():
    course_id = input("Enter course id that you what to show student marks:")
    for student in students:
        for i in range(len(marks)):
            if student['student_id'] == marks[i]['student_id']:
                print(f"{student['student_id']} student:{student['name']} mark:{marks[i][course_id]}")


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
        input_student()
    elif case == 2:
        input_course()
    elif case == 3:
        input_mark()
    elif case == 4:
        list_student()
    elif case == 5:
        list_course()
    elif case == 6:
        list_mark()
    elif case == 7:
        break
    else:
        print("Invalid")
