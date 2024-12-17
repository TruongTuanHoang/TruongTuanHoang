def get_student_info():
    student_id = input("Enter student ID: ")
    student_name = input("Enter student name: ")
    student_dob = input("Enter student date of birth: ")
    return {"id": student_id, "name": student_name, "dob": student_dob}

def get_course_info():
    course_id = input("Enter course ID: ")
    course_name = input("Enter course name: ")
    return {"id": course_id, "name": course_name}

def input_students():
    students = []
    number_of_students = int(input("Number of students: "))
    for student_index in range(number_of_students):
        print(f"Entering information for student {student_index + 1}:")
        students.append(get_student_info())
    return students

def input_courses():
    courses = []
    number_of_courses = int(input("Number of courses: "))
    for course_index in range(number_of_courses):
        print(f"Entering information for course {course_index + 1}:")
        courses.append(get_course_info())
    return courses

def display_courses(course_list):
    for course in course_list:
        print(f"ID: {course['id']}, Name: {course['name']}")

def display_students(student_list):
    for student in student_list:
        print(f"ID: {student['id']}, Name: {student['name']}, DOB: {student['dob']}")

def input_marks(student_list, course_list, marks):
    display_courses(course_list)
    course_id = input("Course ID: ")
    marks[course_id] = {}
    display_students(student_list)
    for student in student_list:
        marks[course_id][student['id']] = float(input(f"Enter mark for student {student['name']} (ID: {student['id']}): "))

def show_marks(student_list, marks):
    course_id = input("Course ID: ")
    for student in student_list:
        mark = marks.get(course_id, {}).get(student['id'], 'N/A')
        print(f"ID: {student['id']}, Name: {student['name']}, Mark: {mark}")

def main():
    marks = {}
    students = []
    courses = []
    while True:
        print("\n0. Exit\n1. Input students\n2. Input courses\n3. List courses\n4. List students\n5. Input marks\n6. Show marks")
        choice = input("Choice: ")
        if choice == "0":
            break
        elif choice == "1":
            students = input_students()
        elif choice == "2":
            courses = input_courses()
        elif choice == "3":
            display_courses(courses)
        elif choice == "4":
            display_students(students)
        elif choice == "5":
            input_marks(students, courses, marks)
        elif choice == "6":
            show_marks(students, marks)

if __name__ == "__main__":
    main()
