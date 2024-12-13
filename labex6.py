def student_record():
    students=[]
    n=int(input("Enter the numebr of students: "))

    for i in range(n):
        student={}
        student['id']=input(f"Enter ID for student {i+1}: ")
        student['name']=input(f"Enter name for student {i+1}: ")
        student['age']=input(f"Enter age for student {i+1}: ")
        student['grade']=input(f"Enter grade for student {i+1}: ")
        students.append(student)

    return students

def search_student(students, student_id):
    
    for student in students:
        if student['id'] == student_id:
            return student
    return None


students = student_record()
search_id = input("Enter the student ID to search: ")

student = search_student(students, search_id)

if student:
    print(f"Student Found: {student}")
else:
    print("Student not found.")