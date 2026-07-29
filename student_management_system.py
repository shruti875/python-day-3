def add_students(students,name,marks):
    students[name] = marks

def show_students(students):
    for name,marks in students.items():
        print(name , ":" , marks)

students = {}

add_students(students,"Shruti",100)
add_students(students,"Aditya",100)
add_students(students,"Sonam",100)
add_students(students,"sara",100)
add_students(students,"Manu",100)

show_students(students)
