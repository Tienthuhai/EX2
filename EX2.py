# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# University class
class University:
    def __init__(self, name):
        self.name = name
        self.faculties = []

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

# Faculty class (inherits from University)
class Faculty(University):
    def __init__(self, university_name, faculty_name):
        super().__init__(university_name)
        self.name = faculty_name
        self.lecturers = []
        self.courses = []

    def add_lecturer(self, lecturer):
        self.lecturers.append(lecturer)

    def add_course(self, course):
        self.courses.append(course)

# Lecturer class (inherits from Person)
class Lecturer(Person):
    def __init__(self, name, age, faculty):
        super().__init__(name, age)
        self.faculty = faculty
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)
        course.lecturer = self

# Course class
class Course:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits
        self.lecturer = None
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        student.courses.append(self)

# Student class (inherits from Person)
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = []

    def register_course(self, course):
        course.add_student(self)

# Demonstration
# Creating a university
uni = University("OpenAI University")

# Creating a faculty
comp_sci_faculty = Faculty(uni.name, "Computer Science")
uni.add_faculty(comp_sci_faculty)

# Creating a lecturer and adding to the faculty
lecturer_john = Lecturer("John Doe", 45, comp_sci_faculty)
comp_sci_faculty.add_lecturer(lecturer_john)

# Creating a course and assigning it to the faculty and lecturer
course_python = Course("Python Programming", 3)
comp_sci_faculty.add_course(course_python)
lecturer_john.assign_course(course_python)

# Creating a student and registering for a course
student_anna = Student("Anna Smith", 20, "S12345")
student_anna.register_course(course_python)

# Output demonstration
print(f"University: {uni.name}")
print("Faculties:")
for faculty in uni.faculties:
    print(f"  - {faculty.name}")
    print("    Lecturers:")
    for lecturer in faculty.lecturers:
        print(f"      * {lecturer.name}")
    print("    Courses:")
    for course in faculty.courses:
        print(f"      * {course.name} (Lecturer: {course.lecturer.name})")

print("\nCourse Enrollments:")
print(f"Course: {course_python.name}")
print("Students enrolled:")
for student in course_python.students:
    print(f"  - {student.name} (ID: {student.student_id})")
