# Student mark management system

students = []
courses = []
marks = {}

# Input number of students
def no_student():
    no_st = int(input("Enter number of students: "))
    return no_st
    
# Input student information
def student_info(no_st):
    for i in range(no_st):
        id_student = input("Enter student id: ")
        name_student = input("Enter student name: ")
        dob = input("Enter student DOB: ")
        print(f"{i+1}: ")
        return (id_student, name_student, dob)
        
# Input number of courses
def no_course():
    no_course = int(input("Enter number of courses: "))
    return no_course
    
# Input course information
def course_info():
    for j in range(no_course):
        id_course = input("Enter course id: ")
        name_course = input("Enter course name: ")
        print(f"{j+1}: ")
        return (id_course, name_course)
        
# Select a course, input marks for student in this course
def input_mark(id_course):
    for id_student in students:
        mark = float(input(f"Enter mark for student {students[id_student]} in course {courses[id_course]}: "))
        return mark
        
# List courses
def course(name_course):
    print("List of courses:")
    for id_course in courses:
        print(f"{courses[id_course]}: {courses[name_course]}")
        
# List students
def student(name_student, dob):
    print("List of courses:")
    for id_student in students:
        print(f"{students[id_student]}: {students[name_student]} - {students[dob]} ")
        
# Show student marks for a given course
def show_student_marks(name_student, name_course):
    for id_course in courses:
        print(f"Student mark in course {courses[id_course]} ({courses[name_course]}) is: ")
        for id_student in students:
            if id_student in marks:
                print(f"{students[id_student][name_student]}: {marks[id_student][id_course]}")
            else:
                print(f"{students[id_student]}: N/A")


