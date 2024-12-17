class Student:
    def __init__(self, student_id, name, dob):
        self.__id = student_id
        self.__name = name
        self.__dob = dob
    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}, DOB: {self.__dob}")
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name

class Course:
    def __init__(self, course_id, name):
        self.__id = course_id
        self.__name = name
    def display(self):
        print(f"ID: {self.__id}, Name: {self.__name}")
    def get_id(self):
        return self.__id

class StudentManagement:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}
    def input_students(self):
        number_of_students = int(input("Number of students: "))
        for i in range(number_of_students):
            print(f"Entering information for student {i + 1}:")
            student_id = input("Enter student ID: ")
            student_name = input("Enter student name: ")
            student_dob = input("Enter student date of birth: ")
            self.students.append(Student(student_id, student_name, student_dob))
    def input_courses(self):
        number_of_courses = int(input("Number of courses: "))
        for i in range(number_of_courses):
            print(f"Entering information for course {i + 1}:")
            course_id = input("Enter course ID: ")
            course_name = input("Enter course name: ")
            self.courses.append(Course(course_id, course_name))
    def display_students(self):
        print("\n--- List of Students ---")
        for student in self.students:
            student.display()
    def display_courses(self):
        print("\n--- List of Courses ---")
        for course in self.courses:
            course.display()
    def input_marks(self):
        self.display_courses()
        course_id = input("Enter course ID to input marks: ")
        if course_id not in self.marks:
            self.marks[course_id] = {}
        self.display_students()
        for student in self.students:
            mark = float(input(f"Enter mark for student {student.get_name()} (ID: {student.get_id()}): "))
            self.marks[course_id][student.get_id()] = mark
    def show_marks(self):
        course_id = input("Enter course ID to view marks: ")
        if course_id not in self.marks or not self.marks[course_id]:
            print("No marks entered for this course.")
            return
        print(f"\n--- Marks for Course ID: {course_id} ---")
        for student in self.students:
            mark = self.marks[course_id].get(student.get_id(), "N/A")
            print(f"ID: {student.get_id()}, Name: {student.get_name()}, Mark: {mark}")

def main():
    management = StudentManagement()
    while True:
        print("\n0. Exit\n1. Input students\n2. Input courses\n3. List courses\n4. List students\n5. Input marks\n6. Show marks")
        choice = input("Choice: ")
        if choice == "0":
            break
        elif choice == "1":
            management.input_students()
        elif choice == "2":
            management.input_courses()
        elif choice == "3":
            management.display_courses()
        elif choice == "4":
            management.display_students()
        elif choice == "5":
            management.input_marks()
        elif choice == "6":
            management.show_marks()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
