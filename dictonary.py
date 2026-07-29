#important part of python is dictonaires used for many things 

# student = {
#     "name": "aditya",
#     "marks": 90,
#     "gender": "male",
#     "city": "mumbai",
#     }

# student["marks"]=100  #update
# student["age"] = 20   #add new
# print(student["name"])

# for key,value in student.items():
#     print(key , ":" , value)

#practice 

def add_employees(employees , name , salary):
    employees[name] = salary

def show_employees(employees):
    for name,salary in employees.items():
       print(name ,":", salary)

def increase_all(employees, amount):
    for name in employees:
        employees[name] += amount

def remove_employee(employees, name):
    if name in employees:
        del employees[name]
    else:
        print("Employee not found")
        

employees = {}

add_employees(employees ,"Shruti" , 5000)
add_employees(employees ,"Aditya" , 5000)

show_employees(employees)

increase_all(employees, 5000)
print(employees)

remove_employee(employees[name == "Shruti"])

