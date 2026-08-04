students_list = [
    {"name": "Alice", "age": 20, "grade": "A" , "id": 1},
    {"name": "Bob", "age": 22, "grade": "B", "id": 2},
    {"name": "Charlie", "age": 19, "grade": "C", "id": 3},
    {"name": "David", "age": 21, "grade": "B", "id": 4},
    {"name": "Eve", "age": 20, "grade": "A", "id": 5},
]


def add_student (name , age , grade):
    for student in students_list:
        if student["name"] == name and student["age"] == age:
            print("Already exists")
            return
    largest = 0
    for student in students_list:
        if student["id"] > largest:
            largest = student["id"]
        
        
    new_student = {
        "name": name,
        "age": age,
        "grade": grade,
        "id" : largest+1
    }
    students_list.append(new_student)
    print("Added")
    print(students_list)
    return
    
def view_students():
    if not students_list :
        print("No student found")
        return
    
    print("-"*40)
    print("-"*14,'Student list',"-"*14)
    print("-"*40)
    for student in students_list:
        print(f"Name: {student['name']}\nAge: {student['age']}\nGrade: {student['grade']}\nID: {student['id']}")
        print("-"*40)

def search_student(student_id):
    for student in students_list:
        if student["id"] == student_id:
            print(f"Name: {student['name']}\nAge: {student['age']}\nGrade: {student['grade']}\nID: {student['id']}")
            return
    print("No student found")

def update_student(student_id):
    
    for student in students_list:
        if student["id"] == student_id:
            print("-"*40)
            print("-"*14,'Current information',"-"*14)
            print("-"*40)
            print(f"Name: {student['name']}\nAge: {student['age']}\nGrade: {student['grade']}\nID: {student['id']}")
            changing_variable = input("What do you want to update? (age or grade): ").lower()
            if changing_variable == "age":
                new_age = int(input("Enter the new age: "))
                student["age"] = new_age
                print("Student updated successfully.")
                return
            elif changing_variable == "grade":
                new_grade = input("Enter new grade: ")
                student["grade"] = new_grade
                print("Student updated successfully.")
                return
            else:
                print("Invalid input")
                return
    print("Invalid student ID.")

def delete_student(student_id):
    for student in students_list:
        if student_id == student["id"]:
            students_list.remove(student)
            print("Information deleted")
            return 
    print("Enter valid ID")
        


print("-"*40)
print("""1. Add student
2. View students
3. Search student
4. Update student
5. Delete student""")
print("-"*40)

try:
    operation = int(input("What do you want to do? : "))
except ValueError:
    print("Invalid operation")
    exit()

if operation == 1:
    name = input("Enter students name: ").strip()

    try:
        age = int(input("Enter student's age: "))
    except ValueError:
        print("Invalid age")
        exit()

    grade = input("Enter student's grade: ").strip()
    add_student(name , age , grade)
elif operation == 2:
    view_students()
elif operation == 3:
    try:
        student_id = int(input("Enter student id: "))
        search_student(student_id)
    except ValueError:
        print("Invalid student ID")
        exit()
elif operation == 4:
    try:
        student_id = int(input("Enter student id: "))
        update_student(student_id)
    except ValueError:
        print("Invalid student ID")
        exit()
elif operation == 5:
    try:
        student_id = int(input("Enter student id: "))
        delete_student(student_id)
    except ValueError:
        print("Invalid student ID")
        exit()
else:
    print("Enter valid operation!")
    



    








           
    
            
