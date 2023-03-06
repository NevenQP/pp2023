students = []

courses = []

marks = [{"student_id": 'none'}]


def inputstudent():
    num_student = int(input("Enter the number of student in the class:"))
    for i in range(num_student):
        student_id = input("Enter the student id:")
        name = input("Enter the student name:")
        dob = input("Enter the student dob:")
        students.append({'student_id': student_id, 'name': name, 'dob': dob})


def inputcours():
    num_course = int(input("Enter the number of course in the class:"))
    for i in range(num_course):
        course_id = input("Enter the course id:")
        name = input("Enter the course name:")
        courses.append({'course_id': course_id, 'name': name})


def inputmark():
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

def listcourse():
    for course in courses:
        print(f"{course['course_id']}: {course['name']}")


def liststudent():
    for student in students:
        print(f"{student['student_id']}: name:{student['name']} dob:{student['dob']}")


def listmark():
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
