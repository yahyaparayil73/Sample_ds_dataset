#Student Management System

#This is a sample assignment by me 


from datetime import datetime as dtm
FILE = "std_mgmt_data.txt"
students = []
std_id = 1



#----------------method to add student----------------

def add_student():
  global std_id
  print("Please enter the students details :")
  roll_no = int(input("Enter the roll number of the student :"))
  name = input("Enter the name of the student :")
  age = int(input("Enter the age of the student :"))
  department = input("Enter the department of the student :")
  marks = int(input("Enter the marks obtained :"))

  student = {
        "student_id": std_id,
        "name": name,
        "roll_no": roll_no,
        "age": age,
        "department": department,
        "marks": marks,
        "timestamp": str(dtm.now())
    }

  students.append(student)
  std_id += 1
  save_students()
  print("Student Added!")

#----------------method to load student----------------

def load_students():
    global students, auto_id
    try:
        with open(FILE, "r") as f:
            for line in f:
                data = eval(line.strip())
                students.append(data)
            if students:
                std_id = students[-1]["student_id"] + 1
    except FileNotFoundError:
        pass

#----------------method to save student----------------

def save_students():
    with open(FILE, "w") as f:
        for s in students:
            f.write(str(s) + "\n")

#----------------method to save student----------------


#----------------method to view students----------------

def view_students():

  print("The list of students are : \n")
  for student in students:
    print("ID:", student['student_id'])
    print("Roll No:", student['roll_no'])
    print("Name:", student['name'])
    print("Age:", student['age'])
    print("Department:", student['department'])
    print("Marks:", student['marks'])
    print("Created Date:", student['timestamp'])
    print("------------------------------------")

#----------------method to view students----------------



#----------------method to update students----------------

def update_students():

  try:
    roll = int(input("Enter roll number to update: "))
  except ValueError:
    print("Invalid input. Please enter a valid roll number.")

  found = False

  for student in students:
      if student['roll_no'] == roll:
          found = True
          print("\nWhich field do you want to update?")
          print("1. Name")
          print("2. Age")
          print("3. Department")
          print("4. Marks")

          choice = int(input("Enter choice: "))

          if choice == 1:
              student['name'] = input("Enter new name: ")
              print("\n Student details updated successfully!")

          elif choice == 2:
              student['age'] = int(input("Enter new age: "))
              print("\n Student details updated successfully!")

          elif choice == 3:
              student['department'] = input("Enter new department: ")
              print("\n Student details updated successfully!")

          elif choice == 4:
              student['marks'] = int(input("Enter new marks: "))
              print("\n Student details updated successfully!")

          else:
              print("Invalid choice")
              break

  if not found:
      print("Student not found!")
  print(students)

#----------------method to update students----------------



#----------------method to delete students----------------

def delete_student():
  roll = int(input("Enter roll number to delete: "))
  found = False
  for student in students:
    if student['roll_no'] == roll:
      found = True
      students.remove(student)
      print("Student deleted successfully!")
      break
  if not found:
    print("Student not found!")
  print(students)

#----------------method to delete students----------------


#----------------method to search students----------------

def search_student():
  name = input("Enter the name of student to search: ")
  found = False
  for student in students:
    if student['name'] == name:
      found = True
      print("Student found!")
      print("student details are given below:")
      print("Roll_no",student['roll_no'])
      print("Name",student['name'])
      print("Age",student['age'])
      print("Department",student['department'])
  if not found:
    print("Student not found!")

#----------------method to search students----------------

#----------------method to view top performing students----------------

def top_students():

  if not students:
    print("No students available.")
  else:
    top_student = sorted(students, key=lambda x: x['marks'], reverse=True)[0]

    print("\nTop Performing Student:")
    print(top_student)

#----------------method to view top performing students----------------


print("Welcome to Student Management System:...................!!!")
print("Enter your login credentials to Continue\n")

while True :                                                                    #loops until the user enters the correct credentials
  username = input("Enter your username: ")
  password = input("Enter your password: ")
  if username == "Entri" and password == "Entri@123":                           # Predefined login credentials (username/password).
      print("Login successful!")                                                # Basic password checking.
      break                                                                     #loop breaks and user enters
  else:
      print("Invalid username or password.")

while True:

    print("\n STUDENT MANAGEMENT SYSTEM")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. View Top Student")
    print("7. Exit")

    choice = int(input(("Enter option: ")))

    if choice == 1:
        add_student()
    elif choice == 2:
        view_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        update_students()
    elif choice == 5:
        delete_student()
    elif choice == 6:
        top_students()
    elif choice == 7:
        print("\n Exiting, Thankuh")
        break
    else:
        print("Invalid choice")

load_students()



#CONCEPTS USED
# GLOBAL VARIABLES
# CONDITIONAL STATEMENTS
# LOOPING STATEMENTS
# FUNCTIONS
# LIST
# DICTIONARY
# FILE HANDLING
# EXCEPITON HANDLING
# MODULES AND LIBRARIES


### please note that i have referred chatgpt and w3 schools for the file handling and the validation section ###




